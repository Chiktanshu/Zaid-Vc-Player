## What's up Kangers
## Don't Kang without Creadits else I will rape your mom

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}

SESSION_NAME = getenv("BQB7VGOulOsQxcDhtv0Dk8ftv62F8tEmK9yTtaNbiVbSDCbKQsEnwP3rXVMV3myFTc065qjn3Qu84IvWdFzZQGAUnSxAJnrcGKQNbjZAh89ty5XEMXrwQ2b_6488nU9RiQb8Co7TKhPQifG3AjDbx9_ZLFqi3ln5Dcna3MshsZTbUur-DmvdgIR9sPW68g7zzkhl-Cdr-GFboQ5KVnmCMFkAnV28claOELVkD0r7blbSF55E81vQ7ZKsHbZx9iYWDsdGxiSecYB63zkMDuR_8kaGOcm1isIDxILPuc9dZGSUx12zIqHYb4A9jkxZBqOSBp1g7NlYsVz101BhMkkWOZO_AAAAAGtsabsA")

if str(getenv("STRING_SESSION2")).strip() == "":
    SESSION2 = str(None)
else:
    SESSION2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    SESSION3 = str(None)
else:
    SESSION3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    SESSION4 = str(None)
else:
    SESSION4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    SESSION5 = str(None)
else:
    SESSION5 = str(getenv("STRING_SESSION5"))

BOT_TOKEN = getenv("BOT_TOKEN", "2141828349:AAGPx5FxotDoFHTcYYcoVR9sPFFreTo_248")
BOT_NAME = getenv("BOT_NAME", "Music Botto")

API_ID = int(getenv("API_ID", "4329428"))
API_HASH = getenv("API_HASH", "da3cda55bca8a7d7cc14e5d294a62d0e")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://Cloner:Cloner@cluster0.cgc6t.mongodb.net/?retryWrites=true&w=majority")
OWNER_NAME = getenv("OWNER_NAME", "Nikarshu")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Canyousenseme_bitch")
ALIVE_NAME = getenv("ALIVE_NAME", "Nikarshu")
BOT_USERNAME = getenv("BOT_USERNAME", "WCC_musicbot")
OWNER_ID = getenv("OWNER_ID", "1802267067")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Hejiullah_wooohuuuu")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "weebs_chitchat")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Weeb_Caffe_Updates")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1802267067").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/a414e2cdfeaa7d4414b89.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-ZAID/Zaid-Vc-Player")
PLAY_IMG = getenv("PLAY_IMG", "https://telegra.ph/file/10b1f781170b1e1867f68.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/b95c13eef1ebd14dbb458.png")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
VIDEO_IMG = getenv("VIDEO_IMG", "https://telegra.ph/file/6213d2673486beca02967.png")
SKIP_IMG = getenv("SKIP_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
NEXT_IMG = getenv("NEXT_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
HEROKU_MODE = getenv("HEROKU_MODE", None)
