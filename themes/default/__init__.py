import xml.etree.ElementTree as ET
from itertools import groupby

import htpy
from markupsafe import Markup
from pelican.contents import Article


class ArticleProxy(Article):
    @property
    def title(self) -> str:
        if hasattr(self, "title"):
            return self.title
        return ""


class Entities:
    copy = Markup("&copy;")
    middot = Markup("&middot;")


class Renderable(str):
    def render(self) -> str:
        return self


def _pelican_html(value: str) -> Markup:
    return Markup(value)  # noqa: S704 - Trusted, repository-authored HTML.


def _article_link(href_base: str, article_: ArticleProxy) -> htpy.Renderable:
    return htpy.li[
        htpy.a(href=f"{href_base}/{article_.url}")[_pelican_html(article_.title)],
        " ",
        htpy.small["(", article_.locale_date, ")"],
    ]


def _footer(author: str) -> htpy.Renderable:
    return htpy.footer[htpy.hr, htpy.p[Entities.copy, " ", author]]


def _head(context: dict, title: str = "") -> htpy.Renderable:
    href_base = "" if context["RELATIVE_URLS"] else context["SITEURL"]
    return htpy.head[
        htpy.meta(charset="utf-8"),
        htpy.meta(
            content="width=device-width, initial-scale=1, shrink-to-fit=no",
            name="viewport",
        ),
        _stylesheet(
            href_base,
            context["THEME_STATIC_DIR"],
            "main.css",
        ),
        _stylesheet(
            href_base,
            context["THEME_STATIC_DIR"],
            "code-highlight.css",
        ),
        htpy.title[title or context["SITENAME"]],
    ]


def _header(
    href_base: str,
    site_name: str,
    chrono_active: bool,
    alpha_active: bool,
) -> htpy.Renderable:
    return htpy.header[
        htpy.p(".site-name")[
            htpy.strong[site_name],
            " ",
            Entities.middot,
            " ",
            htpy.a(href=f"{href_base}/")["chrono index"]
            if chrono_active
            else "chrono index",
            " ",
            Entities.middot,
            " ",
            htpy.a(href=f"{href_base}/alpha")["alpha index"]
            if alpha_active
            else "alpha index",
        ],
        htpy.hr,
    ]


def _stylesheet(
    href_base: str, theme_static_dir: str, stylesheet: str
) -> htpy.Renderable:
    return htpy.link(
        href=f"{href_base}/{theme_static_dir}/{stylesheet}",
        rel="stylesheet",
        type="text/css",
    )


def alpha(context: dict) -> htpy.Renderable:
    href_base = "" if context["RELATIVE_URLS"] else context["SITEURL"]
    articles: list[ArticleProxy] = context["articles"]
    return htpy.html(lang="en")[
        _head(context),
        htpy.body[
            _header(href_base, context["SITENAME"], True, False),
            htpy.main[
                htpy.ul[
                    (
                        _article_link(href_base, article_)
                        for article_ in sorted(articles, key=lambda x: x.title.lower())
                    )
                ]
            ],
            _footer(context["AUTHOR"]),
        ],
    ]


def article(context: dict) -> htpy.Renderable:
    href_base = "" if context["RELATIVE_URLS"] else context["SITEURL"]
    article_: ArticleProxy = context["article"]
    page_title = f"{context['SITENAME']} / {_pelican_html(article_.title).striptags()}"
    return htpy.html(lang="en")[
        _head(context, page_title),
        htpy.body[
            _header(href_base, context["SITENAME"], True, True),
            htpy.main[
                htpy.h1[_pelican_html(article_.title)],
                htpy.p["by ", article_.author.name, " on ", article_.locale_date],
                _pelican_html(article_.content),
            ],
            _footer(context["AUTHOR"]),
        ],
    ]


def default(context: dict) -> htpy.Renderable:
    return htpy.html(lang="en")[_head(context)]


def drafts(context: dict) -> htpy.Renderable:
    href_base = "" if context["RELATIVE_URLS"] else context["SITEURL"]
    drafts_: list[ArticleProxy] = context["drafts"]
    return htpy.html(lang="en")[
        _head(context),
        htpy.body[
            _header(href_base, context["SITENAME"], True, True),
            htpy.main[
                htpy.h1["Drafts"],
                htpy.ul[(_article_link(href_base, article_) for article_ in drafts_)],
            ],
            _footer(context["AUTHOR"]),
        ],
    ]


def index(context: dict) -> htpy.Renderable:
    href_base = "" if context["RELATIVE_URLS"] else context["SITEURL"]
    articles: list[ArticleProxy] = context["articles"]
    return htpy.html(lang="en")[
        _head(context),
        htpy.body[
            _header(href_base, context["SITENAME"], False, True),
            htpy.main[
                htpy.h1["All articles"],
                (
                    (
                        htpy.h2[year],
                        htpy.ul[
                            (
                                _article_link(href_base, article_)
                                for article_ in articles
                            )
                        ],
                    )
                    for year, articles in groupby(articles, key=lambda x: x.date.year)
                ),
            ],
            _footer(context["AUTHOR"]),
        ],
    ]


def rss(context: dict) -> Renderable:
    root = ET.Element(
        "rss", attrib={"version": "2.0", "xmlns:atom": "http://www.w3.org/2005/Atom"}
    )
    channel = ET.SubElement(root, "channel")
    channel_title = ET.SubElement(channel, "title")
    channel_title.text = context["SITENAME"]
    channel_link = ET.SubElement(channel, "link")
    channel_link.text = context["FEED_DOMAIN"]
    ET.SubElement(
        channel,
        "atom:link",
        href=f"{context['FEED_DOMAIN']}/{context['page'].url}",
        rel="self",
        type="application/rss+xml",
    )
    channel_description = ET.SubElement(channel, "description")
    channel_description.text = context["SITESUBTITLE"]

    articles: list[ArticleProxy] = context["articles"]
    for article_ in articles:
        item = ET.SubElement(channel, "item")
        title = ET.SubElement(item, "title")
        title.text = _pelican_html(article_.title).striptags()
        link = ET.SubElement(item, "link")
        link.text = f"{context['FEED_DOMAIN']}/{article_.url}"
        guid = ET.SubElement(item, "guid", isPermaLink="false")
        guid.text = f"/{article_.url}"
        pubdate = ET.SubElement(item, "pubDate")
        pubdate.text = article_.date.strftime("%a, %d %b %Y %H:%m:%S %z")
        description = ET.SubElement(item, "description")
        description.text = article_.content

    return Renderable(ET.tostring(root, encoding="unicode", xml_declaration=True))
