import os

# WARNING Feeds generated without SITEURL set properly may not be valid
SITEURL = "https://blog.subtlecoolness.com"

# WARNING No timezone information specified in the settings. Assuming your timezone is
# UTC for feed generation.
TIMEZONE = "America/Chicago"

# default path is working directory, so specify to 'content' directory
PATH = "content"

# set the theme
THEME = "themes/default"

# I have .html and .xml template files
TEMPLATE_EXTENSIONS = [
    ".html",
    ".xml",
]

# CRITICAL UndefinedError: 'pelican.contents.Article object' has no attribute 'author'
AUTHOR = "William Jackson"

# default location to save articles is at the top of the output directory
ARTICLE_SAVE_AS = "{date:%Y/%m/%d}/{urlname}.html"
ARTICLE_URL = "{date:%Y/%m/%d}/{urlname}"
DRAFT_SAVE_AS = "drafts/{date:%Y/%m/%d}/{urlname}.html"
DRAFT_URL = "drafts/{date:%Y/%m/%d}/{urlname}"

# I don't want the default archive, author, and category pages
ARCHIVES_SAVE_AS = ""
AUTHOR_SAVE_AS = ""
AUTHORS_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""
CATEGORY_SAVE_AS = ""
TAGS_SAVE_AS = ""

# I don't want any of the default feeds
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
FEED_ALL_ATOM = None
TRANSLATION_FEED_ATOM = None

# I don't want to remember to delete the output directory before every build
DELETE_OUTPUT_DIRECTORY = True

# I don't like the default date format
DEFAULT_DATE_FORMAT = "%Y-%m-%d"

# The blog needs a name
SITENAME = "Subtle Coolness"

# SITESUBTITLE is used in the rss feed
SITESUBTITLE = "An all-around decent fellow"

# set RELATIVE_URLS from environment, default False
RELATIVE_URLS = os.getenv("RELATIVE_URLS", "false").lower() in (
    "1",
    "on",
    "true",
    "yes",
)

# some files need to land in special locations
EXTRA_PATH_METADATA = {
    "images/gitignore.txt": {
        "path": ".gitignore",
    },
    "images/keybase.txt": {
        "path": "keybase.txt",
    },
}
