BASE_URL = 'https://api.roblox.com/'

# API endpoints
USER_ENDPOINT = f'{BASE_URL}users/'
GROUP_ENDPOINT = f'{BASE_URL}groups/'
ASSET_ENDPOINT = f'{BASE_URL}assets/'

# Error messages
INVALID_USER_ID_MSG = 'Invalid user ID provided.'
GROUP_NOT_FOUND_MSG = 'Specified group not found.'

# Timeout settings
REQUEST_TIMEOUT = 10  # seconds

# Roles and permissions
ROLE_MEMBER = 'Member'
ROLE_ADMIN = 'Admin'
ROLE_OWNER = 'Owner'

# Asset types
ASSET_TYPE_IMAGE = 'Image'
ASSET_TYPE_SOUND = 'Audio'
ASSET_TYPE_MODEL = 'Model'
ASSET_TYPE_VIDEO = 'Video'
ASSET_TYPE_PLACE = 'Place'

# Default values
DEFAULT_PAGE_SIZE = 50
MAX_PAGE_SIZE = 100

# Miscellaneous
APP_VERSION = '1.0.0'
USER_AGENT = 'roblox-tools/1.0.0'
