from Zaid import Zaid, BOT_USERNAME
from Config import Config
from telethon import events, Button

PM_START_TEXT = """
ʜᴇʏᴀ! {}
━━━━━━━𝘿𝞓𝙍𝙎𝙃𝞓𝞟𝞓 ━━━━━━━
๏ ᴀ ғᴀꜱᴛ ᴀɴᴅ ᴩᴏᴡᴇʀғᴜʟ ᴍᴜꜱɪᴄ ᴩʟᴀʏᴇʀ ʙᴏᴛ ᴡɪᴛʜ ꜱᴏᴍᴇ ᴀᴡᴇꜱᴏᴍᴇ ғᴇᴀᴛᴜʀᴇꜱ.
┏━━━━━━━━━━━━━━━━━┓
┣★ ᴄʀᴇᴀᴛᴏʀ : @Kailas_vg
┣★ ꜱᴜᴘᴘᴏʀᴛ : @About_Kailas
┣★ ᴜᴘᴅᴀᴛᴇꜱ : @Pranav_Updates
┣★ ɴᴇᴛᴡᴏʀᴋ : @Hell_Federation_TG
┗━━━━━━━━━━━━━━━━━┛
๏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʜᴇʟᴩ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴛᴏ ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴍʏ ᴄᴏᴍᴍᴀɴᴅꜱ.
━━━━━━━𝘿𝞓𝙍𝙎𝙃𝞓𝞟𝞓 ━━━━━━━
"""

@Zaid.on(events.NewMessage(pattern="^[?!/]start$"))
async def start(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_private:
       await event.client.send_file(event.chat_id,
             Config.START_IMG,
             caption=PM_START_TEXT.format(event.sender.first_name), 
             buttons=[
        [Button.url("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀᴛ", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("👨‍💻 ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", "https://t.me/about_kailas/36")],
        [Button.url("🗣️ ꜱᴜᴘᴘᴏʀᴛ", f"https://t.me/{Config.SUPPORT}"), Button.url("🍁 ɴᴇᴛᴡᴏʀᴋ", f"https://t.me/{Config.CHANNEL}")],
        [Button.inline("ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅꜱ", data="help")]])
       return

    if event.is_group:
       await event.reply("**𝗛𝗲𝘆𝗮 𝗜 𝗮𝗺 𝘀𝘁𝗶𝗹𝗹 𝗮𝗹𝗶𝘃𝗲✅ :) 𝗣𝗠 𝗺𝗲 𝗶𝗳 𝘆𝗼𝘂 𝗵𝗮𝘃𝗲 𝗮𝗻𝘆 𝗾𝘂𝗲𝘀𝘁𝗶𝗼𝗻𝘀 𝗼𝗻 𝗵𝗼𝘄 𝘁𝗼 𝘂𝘀𝗲 𝗺𝗲!**")
       return



@Zaid.on(events.callbackquery.CallbackQuery(data="start"))
async def _(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_private:
       await event.edit(PM_START_TEXT.format(event.sender.first_name), buttons=[
        [Button.url("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀᴛ", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("👨‍💻 ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", "https://t.me/about_kailas/36")],
        [Button.url("🗣️ ꜱᴜᴘᴘᴏʀᴛ", f"https://t.me/{Config.SUPPORT}"), Button.url("🍁 ɴᴇᴛᴡᴏʀᴋ", f"https://t.me/{Config.CHANNEL}")],
        [Button.inline("ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅꜱ", data="help")]])
       return
