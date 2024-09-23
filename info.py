# ©️biisal jai shree krishna 😎
from os import environ

API_ID = environ.get("API_ID", "28776072")
API_HASH = environ.get("API_HASH", "b3a786dce1f4e7d56674b7cadfde3c9d")
BOT_TOKEN = environ.get("BOT_TOKEN", "7063596308:AAFSqoH9xJ88TwjVrHISPbRtCQOvoz_YXFM")
BOT_NAME = environ.get("BOT_NAME", "FTM GPT")
ADMIN = int(environ.get("ADMIN", "7042535787"))
CHAT_GROUP = int(environ.get("CHAT_GROUP", "-1002363780372"))
ADMIN_NAME = environ.get("ADMIN_NAME", "╚» 𝔽𝕋𝕄 𝔻𝔼𝕍𝔼𝕃𝕆ℙ𝔼ℝ«╝")
LOG_CHANNEL = environ.get("LOG_CHANNEL", "-1002209201816")
MONGO_URL = environ.get("MONGO_URL", "mongodb+srv://ftm:ftm@ftmbot.pb9ec.mongodb.net/?retryWrites=true&w=majority&appName=ftmbot")
AUTH_CHANNEL = int(
    environ.get("AUTH_CHANNEL", "-1002175511107")
)  # add your channel id for force subscribe
FSUB = environ.get("FSUB", True)
STICKERS_IDS = (
    "CAACAgQAAxkBAAEK99dlfC7LDqnuwtGRkIoacot_dGC4zQACbg8AAuHqsVDaMQeY6CcRojME"
).split()
COOL_TIMER = 20  # keep this atleast 20
ONLY_SCAN_IN_GRP = environ.get(
    "ONLY_SCAN_IN_GRP", True
)  # If IMG_SCAN_IN_GRP is set to True, image scanning is restricted to your support group only. If it's False, the image scanning feature can be used anywhere.
REACTIONS = ["❤️‍🔥", "⚡", "🔥"]
