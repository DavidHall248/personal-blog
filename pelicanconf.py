AUTHOR = 'David Hall'
SITENAME = "David Hall's Blog"
SITEURL = 'https://davidhall.pages.dev'

PATH = "content"

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

THEME = 'themes/Flex'
THEME_COLOR = "dark"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PAGE_PATHS = ['pages']
DISPLAY_PAGES_ON_MENU = True

# Blogroll
LINKS = (
    ("work", SITEURL+"/category/work.html"),
    ("projects", SITEURL+"/category/projects.html"),
#    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
#    ("You can modify those links in your config file", "#"),
)

# Social widget
#SOCIAL = (
#    ("You can add links in your config file", "#"),
#   ("Another social link", "#"),
#)

DEFAULT_PAGINATION = 5

ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'