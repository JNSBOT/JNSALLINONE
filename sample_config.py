import os

class Config(object):
    # get a token from https://chatbase.com
    CHAT_BASE_TOKEN = os.environ.get("CHAT_BASE_TOKEN", "")
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
    # The Telegram API things
    USER_NAME = os.environ.get("USER_NAME", "")
    APP_ID = int(os.environ.get("APP_ID", 12345))
    API_HASH = os.environ.get("API_HASH")
    # Get these values from my.telegram.org
    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())
    # Banned Unwanted Members..
    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "")
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    # https://t.me/hevcbay/951
    OUO_IO_API_KEY = ""
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    # watermark file
    DEF_WATER_MARK_FILE = "Renamed by @turboremaxbot"
    # Sql Database url
    DB_URI = os.environ.get("DATABASE_URL", "")
    #
    ARIA_TWO_STARTED_PORT = int(os.environ.get("ARIA_TWO_STARTED_PORT", 6800))
    EDIT_SLEEP_TIME_OUT = int(os.environ.get("EDIT_SLEEP_TIME_OUT", 15))
    MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START = int(os.environ.get("MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START", 600))
    MAX_TG_SPLIT_FILE_SIZE = int(os.environ.get("MAX_TG_SPLIT_FILE_SIZE", 2097152000))
    # add config vars for the display progress
    FINISHED_PROGRESS_STR = os.environ.get("FINISHED_PROGRESS_STR", "◾")
    UN_FINISHED_PROGRESS_STR = os.environ.get("UN_FINISHED_PROGRESS_STR", "◽")
    # add offensive API
    TG_OFFENSIVE_API = os.environ.get("TG_OFFENSIVE_API", None)
    CUSTOM_FILE_NAME = os.environ.get("CUSTOM_FILE_NAME", "")
    LEECH_COMMAND = os.environ.get("LEECH_COMMAND", "leech@torrentl33ch3rbot")
    YTDL_COMMAND = os.environ.get("YTDL_COMMAND", "ytdl@torrentl33ch3rbot")
    RCLONE_CONFIG = os.environ.get("RCLONE_CONFIG", "")
    DESTINATION_FOLDER = os.environ.get("DESTINATION_FOLDER", "TorrentLeech-Gdrive")
    GLEECH_COMMAND = os.environ.get("GLEECH_COMMAND", "gleech@torrentl33ch3rbot")
    INDEX_LINK = os.environ.get("INDEX_LINK", "")
    TELEGRAM_LEECH_COMMAND_G = os.environ.get("TELEGRAM_LEECH_COMMAND_G", "tleech@torrentl33ch3rbot")
    CANCEL_COMMAND_G = os.environ.get("CANCEL_COMMAND_G", "cancel@torrentl33ch3rbot")
    GET_SIZE_G = os.environ.get("GET_SIZE_G", "getsize")
    STATUS_COMMAND = os.environ.get("STATUS_COMMAND", "status@torrentl33ch3rbot")
    SAVE_THUMBNAIL = os.environ.get("SAVE_THUMBNAIL", "savethumb@torrentl33ch3rbot")
    CLEAR_THUMBNAIL = os.environ.get("CLEAR_THUMBNAIL", "clearthumb@torrentl33ch3rbot")

