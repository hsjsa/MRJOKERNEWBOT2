# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open("{}/mrjoker/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 1383845  # integer value, dont use ""
    BOT_ID = "1384019653"
    API_HASH = "0e3d2c299cc3c5cc26c283cecd2eb97c"
    #STRING_SESSION = "BQATALeWXSrQ6h6YS4cizq4hvDZ51ZJdDxNxuvDiI9iOlOlcagsMBMOveBfHE-iuXvWJaReJM6wWoY53XZEgjkT8hDPjXgubUZf-5AjRusUbYGN2a6Hoiq8N0qfajejHIz5fxgG2Gp6CI9rzNMKAJWx5QEjaZXibeNMAFeX_mWXKYovzNg7EuvQ7lUTcob7_3xXxTQHXTDiygpgE5FGFNkEQF8fajpWjQnHS0ew7_TOaoXT1SnZ-O94gLLgHoVtTRBDTV3OkJLOQapJFtO7mTTQgIFiPeDaGk6fYv3Kg41z8WaAAUuxwL96qJgDzRc1jNF_8JPa3d-Kts8-WXcBbkX0IQ3OqNQA"
    TOKEN = "1384019653:AAGeq9rGVQqlTcP45sWZDhW2oEQ2YZ8bmGs"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    BOT_USERNAME = "Mrjokerlk_bot"
    OWNER_ID = 1131653685   # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "kavinduaj"
    ARQ_API_URL = "https://thearq.tech"
    ARQ_API_KEY = "ULYTMW-MOFYPS-KLWEUW-KNQWVO-ARQ"
    SUDO_USERS = 1131653685
    SUPPORT_USERS = 1131653685
    WHITELIST_USERS = 1131653685
    SUPPORT_CHAT = "lkhitech"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001329348574
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001329348574
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:xsrDxZxEs8pLhCudhkHF@containers-us-west-12.railway.app:7044/railway"  
    REDIS_URI = "redis://default:oCSncAKDtwhxRKJvl715@containers-us-west-11.railway.app:5601"
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = "DFOm~tAD3jGW_l_pxisfl1FETDTytFaz831fAciaKZg9kCoAYuPAP0lYSO5QDdbC"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"
    OPENWEATHERMAP_ID = "d1771e86e5540a19ac86af534754cb13"

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = "1131653685"
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = "1131653685"
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = "1131653685"
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = "1131653685"
    WOLVES = "1131653685"
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "GFO4UK7F4NGUMYTT"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "1AW4Q9DTFF4"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "xyz"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "xyz"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None
    YOUTUBE_API_KEY=""
    INFOPIC =""
    TEMP_DOWNLOAD_DIRECTORY = "./"
    REM_BG_API_KEY = "gQXc1AuEraj3numU671LhNhW"
    MONGO_DB_URI = "mongodb+srv://mrjoker:kaj@cluster0.ooq0i.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    MONGO_DB = "mrjoker"


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
