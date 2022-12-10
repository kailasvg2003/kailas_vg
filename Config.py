import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "22029156"))
    API_HASH = os.environ.get("API_HASH", "7c7d75736193b71d40b00dc0b0981725")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5948256402:AAFDSk4Ozd8R0LacYtOG8ge9Y-GDFadSvYI")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOKIBuydr_srFpcv98JMZUl783ev-MUI5-Z7zqdRvfZ4ttub8th696TRlsuWGiT03GXk-ngzHrGshoT7Aor0200S2qiiE9GKJrtJXyiNn9PaRrDBZ2hRxwYP0txeXu8Ky-k0nJZ-JkER6We_2GUkl_M3cKHjgNY5fZOY5VC7z-g2tSmuzLNZh55PweEiDmr48zrWyQtiXiqWgvpBp6Vmnvbgcbul1UYxBKOvlzXFjaDkxYcxXxyvCFdPvlRXg8oFz3zA2hlu_aVbPOZxphnIIn710lnXroqi9wfidvBHIqNh2b260VGe_GvSKEpEHZMd6WVXnTz9_aj5K2rAEzCyyK8khOFs=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Darshana_Music_Bot"
    SUPPORT = os.environ.get("SUPPORT", "Pranav_support_chat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "Hell_Federation_TG") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/081c9b5aa623eb60c5d7f.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/c9dbb1f7ff00665698e7d.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "1880216154")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
