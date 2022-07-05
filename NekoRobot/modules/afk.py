from telethon import events, Button, custom
import re, os
from NekoRobot.events import register
from NekoRobot import telethn as tbot
from NekoRobot import telethn as tgbot
PHOTO = "https://telegra.ph/file/2f44c5a7a2d64fa884647.jpg"
@register(pattern=("/about"))
async def awake(event):
  NEKO = """
         ◈ Hey Darling,
                    This is Yor ❤️‍🔥

➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖

Yor Info ➣ :-

◈ I Am A Anime Themed Advance Group Management Bot With A Lot Of Sexy Features.
 ‣ A powerful Group Management bot built to help you manage your group easily & to protect your group from scammers & spammers.

🤖 What can i do :
 ‣ I can restrict users.
 ‣ I can greet users with customisable welcome messages & even set a  group's rules.
 ‣ I can warn users until they reach max warns, with each predefined actions such as ban, mute, kick, etc.
 ‣ I have an advanced anti-flood system.
 ‣ I have a note keeping system, blacklists, and even predetermined replies on certain keywords.
 ‣ I check for admins permission before executing any command & more stuffs.

➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖


◈ Check The Buttons To Know About Me More.

"""
  
  BUTTON = [[Button.url("♥️ My Master", "https://t.me/MrSumit004"), Button.url("Start", "https://t.me/YorForger_Xbot?start")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=NEKO,  buttons=BUTTON)
