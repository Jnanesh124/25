# Thanks @Codeflix_Bots

import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6570037316:AAFv5dv2LjbVdjwFDFdAN9N1ezSVMmBqVMI")

APP_ID = int(os.environ.get("APP_ID", "22231458"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "f7cb57cc5f91c944f3ddeb8a60a99466")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002211186535"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6331847574"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://easyeasy740:easyeasy740@cluster0.1shrvws.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#Shortner (token system) 

SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "zipshort.net")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "43fb16ff834e0026f99fe1083b70d768b631802b")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 86400)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID","https://t.me/How_to_open_link_rockersbot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002212636543"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>ʜᴇʟʟᴏ {first} u need to verify below link\n\nthen u get direct sex video</b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6852649461").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "more video uploded in below group \n\n 𝐒𝐨 𝐩𝐥𝐞𝐚𝐬𝐞 𝐣𝐨𝐢𝐧 𝐦𝐲 group 𝐟𝐢𝐫𝐬𝐭 𝐚𝐧𝐝 𝐜𝐥𝐢𝐜𝐤 𝐨𝐧 “𝐍𝐨𝐰 𝐂𝐥𝐢𝐜𝐤 𝐡𝐞𝐫𝐞” 𝐛𝐮𝐭𝐭𝐨𝐧....!")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "join here :- https://t.me/+rngXtnHMa_k3NjY9\n\njoin here :- https://t.me/+rngXtnHMa_k3NjY9\n\njoin here :- https://t.me/+rngXtnHMa_k3NjY9"

ADMINS.append(OWNER_ID)
ADMINS.append(6331847574)

LOG_FILE_NAME = "codeflixbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
