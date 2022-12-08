import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "22029156"))
    API_HASH = os.environ.get("API_HASH", "7c7d75736193b71d40b00dc0b0981725")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5948256402:AAFDSk4Ozd8R0LacYtOG8ge9Y-GDFadSvYI")
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Darshana_Music_Bot")
    SUPPORT = os.environ.get("SUPPORT", "Pranav_support_chat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "Hell_Federation_TG") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/081c9b5aa623eb60c5d7f.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/c9dbb1f7ff00665698e7d.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5856895717")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
