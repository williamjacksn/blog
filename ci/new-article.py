import argparse
import datetime
import pathlib
import zoneinfo

ARTICLE_TEMPLATE = """title: {}
urlname: {}
date: {}
status: draft

- apostrophe: &#x02bc;
"""


class Args:
    title: str
    urlname: str


def parse_args() -> Args:
    parser = argparse.ArgumentParser()
    parser.add_argument("title")
    parser.add_argument("urlname")
    return parser.parse_args(namespace=Args())


def main() -> None:
    zone = zoneinfo.ZoneInfo("America/Chicago")
    now = datetime.datetime.now(zone)
    args = parse_args()
    target = (
        pathlib.Path("content/articles")
        / str(now.year)
        / f"{now:%m}"
        / f"{now:%Y-%m-%d}-{args.urlname}.md"
    )
    if target.exists():
        print(f"The article at {target} already exists")
    else:
        article_date = now.strftime("%Y-%m-%d %H:%M %z")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(
            ARTICLE_TEMPLATE.format(args.title, args.urlname, article_date),
            newline="\n",
        )


if __name__ == "__main__":
    main()
