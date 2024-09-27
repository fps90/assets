import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID","16228886"))
API_HASH = getenv("API_HASH","b7de6ba01d7af6fc2d99375b5fbd0f82")
BOT_TOKEN = getenv("BOT_TOKEN","5538104001:AAHH9a9A3CtT9umPFd0TLZbSfCYjgu8H7xU")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://omsnkok:muntazer@cluster0.ywxsjao.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "9999"))
LOGGER_ID = int(getenv("LOGGER_ID", "-1001854110934"))
BOTADDLOGS = int(getenv("BOTADDLOGS", "-1001854110934")) # LOGGER_ID Id Also Use No Problem
GBAN_LOGS = int(getenv("GBAN_LOGS", "-1001854110934"))
GCAST_USERS = list(map(int, getenv("GCAST_USERS", "2105971379 7137269276 7045191057").split()))
OWNER_ID = int(getenv("OWNER_ID", 5186954055))
OWNER = int(getenv("OWNER", 5186954055))
OWNER_USERNAME = getenv("OWNER_USERNAME","sultan11100")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
UPSTREAM_REPO = getenv("UPSTREAM_REPO","https://github.com/AbhiModszYT/AnieXEricaMusic")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN",None)
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/SuperBanSBots")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/AM_YTSUPPORT")
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "5400"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", 7000))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", 7000))
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "9999")) 
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2a230af10e0a40638dc77c1febb47170")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "7f92897a59464ddbbf00f06cd6bda7fc")
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "3000"))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 5242880000))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 5242880000))
STRING1 = getenv("STRING_SESSION", "AgCIVfMAa_Q4giosRUF8lDN7m_Q4m6WeeCM1anQsYqQlsDIkNIljMU7Pgc9mQmF5R1TMKiRb1AF72PwqePJUowquYBCXG1vi4rC325zNOKjI385z5A18aFQx37DNg_E_ArHUzsLfF900n5aJMbVnzAqKUMco4c6sjY6u6NKsUOTWXrOkMMvwgHMNXZSM7SiHR5a9Sxy4RfnYYKVD-Y3leoJ_AA5ppJXTLVs58oTrUnnxqmNhpzFzV3DwuJTuLdHX0yK2H5tHLkLzlOxw2gaW_0G2OZZUHBpi0DjbzmU4nFOSWf8YHJ8xJ5OwWRyBL0_hCJ_BY9gfu8vYL9GFkmgEZb-TCLfPaQAAAAFBhL7oAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSION6", None)
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
AMBOT = [
    "🔎",
    "🔍",
    "🧪",
    "ᴘʟꜱ ᴡᴀɪᴛ..",
    "ᴘʀᴏᴄᴇꜱꜱɪɴɢ..",
]

START_IMG_URL = getenv("START_IMG_URL", "https://i.ibb.co/82xJS5p/image.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://i.ibb.co/HnC5B2R/image.jpg")
PLAYLIST_IMG_URL = "https://i.ibb.co/Cn9P7KK/image.jpg"
STATS_IMG_URL = getenv("STATS_IMG_URL", "https://i.ibb.co/Dk9Krtk/image.jpg")
TELEGRAM_AUDIO_URL = "https://i.ibb.co/Y3FC6RT/image.jpg"
TELEGRAM_VIDEO_URL = "https://i.ibb.co/PcJNLPm/image.jpg"
STREAM_IMG_URL = "https://i.ibb.co/v3xJt0s/image.jpg"
SOUNCLOUD_IMG_URL = "https://i.ibb.co/R3MPzZS/image.jpg"
YOUTUBE_IMG_URL = "https://i.ibb.co/cTjYH9g/image.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://i.ibb.co/D8bK6cF/image.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
