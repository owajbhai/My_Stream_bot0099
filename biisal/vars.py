# (c) adarsh-goel (c) biisal (c) TechifyBots
import os
from os import getenv, environ
from dotenv import load_dotenv

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '23621595'))
    API_HASH = str(getenv('API_HASH', 'de904be2b4cd4efe2ea728ded17ca77d'))
    BOT_TOKEN = str(getenv('BOT_TOKEN' , ''))
    PICS = (environ.get('PICS', 'https://image.zaw-myo.workers.dev/image/ba994fdf-9c4a-4759-abb5-8a0ef9f19a5e')).split()
    name = str(getenv('name', 'movieLover1_Bot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1002245217353'))
    NEW_USER_LOG = int(getenv('NEW_USER_LOG', '-1001860172104'))
    PORT = int(getenv('PORT', '8080'))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = [int(x) for x in os.environ.get("OWNER_ID", "1249672673").split()]
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'botmaster55'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME')) #dont need to fill anything here
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', 'https://horrible-fania-bhaiforik76-baf3f629.koyeb.app/')) if not ON_HEROKU or getenv('FQDN', 'https://liquid-guglielma-bhaiforik76-551d8f99.koyeb.app/') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',True))
    if HAS_SSL:
        URL = "https://horrible-fania-bhaiforik76-baf3f629.koyeb.app/".format(FQDN)
    else:
        URL = "https://horrible-fania-bhaiforik76-baf3f629.koyeb.app/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://mongodb011:rxXV4pGzxLJgxaXQ@cluster0.undjh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', 'SpyRadioHD')) 
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1002245217353")).split()))   
    BAN_CHNL = list(set(int(x) for x in str(getenv("BAN_CHNL", "-1002245217353")).split()))   
    BAN_ALERT = str(getenv('BAN_ALERT' , '<b>ʏᴏᴜʀ ᴀʀᴇ ʙᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ.ᴄᴏɴᴛᴀᴄᴛ @botmaster55 ᴛᴏ ʀᴇsᴏʟᴠᴇ ᴛʜᴇ ɪssᴜᴇ!!</b>'))
    SHORTLINK = is_enabled('SHORTLINK', False)
    SHORTLINK_URL = getenv('SHORTLINK_URL', 'arolinks.com')

    SHORTLINK_API = getenv('SHORTLINK_API', 'd6a2a1bae0a25c4aa2d4d3c3ad364d6306995a37')














