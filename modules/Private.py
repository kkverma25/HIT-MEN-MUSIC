
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters
import signal
import os
import sys

HOME_TEXT = "<b>ʜᴇʏ, [{}](tg://user?id={})\n\n . 𝐇𝐄𝐘  𝐌𝐘 𝐍𝐀𝐌𝐄 𝐈𝐒 𝐃𝐄𝐕𝐈𝐋 𝐃𝐀𝐃 𝐌𝐔𝐒𝐈𝐂.\n 𝐀𝐃𝐃 𝐌𝐄 𝐈𝐍 𝐘𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 & 𝐏𝐋𝐀𝐘 𝐒𝐎𝐍𝐆.\n𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐄𝐑= [𝐄𝐕𝐄𝐑𝐄𝐓𝐓](https://t.me/YOUR_DEVIL_DAD) .\n\n ..........🖤🎧🖤......."   


HELP = """
🎧 <b>I Can Play Musics On VoiceChats 🤪</b>

🎶 **Common Commands**:
• `/song` __Download Song from youtube__
• `/play`  __Play song you requested__
• `/help` __Show help for commands__
• `/dplay` __Play song you requested via deezer__
• `splay` __Play song you requested via jio saavn__
• `/ytplay` __Play song directly from youtube server__
• `/search` __Search video songs links__
• `/current` __Show now playing__
• `/playlist` __Show now playing list__
• `/video` __Downloads video song quickly__
🎶 **Admin Commands**:
• `/player`  __Open music player settings panel__
• `/pause` __Pause song play__
• `/skip` __Skip next song__
• `/resume`  __Resume song play__
• `/userbotjoin`  __Invites assistant to your chat__
• `/end` __Stops music play__
• `/admincache` __Refresh list of admins with vc power__
© Powered By 
[ __@world_wide_chattt || @world_wide_chattt__ ]
"""



@Client.on_message(filters.command('start'))
async def start(client, message):
    buttons = [
       [
                InlineKeyboardButton('⚡𝕮𝖍𝖆𝖓𝖓𝖊𝖑⚡', url='https://t.me/ABOUT_ARVI'),
                InlineKeyboardButton('乂❤₲ⱤØɄ₱❤乂', url='https://t.me/world_wide_chattt')
                ],[
                InlineKeyboardButton('👸🇪🅻🅸👸', url='https://t.me/Eliana_072'),
                InlineKeyboardButton('👸🇦🆁🆅🅸👸', url='https://t.me/FOREVER_ANGEL_0')
                ],[
                InlineKeyboardButton('║█🇦𝑫𝑫 🇲𝑬 🇹𝑶 🇾𝑶𝑼𝑹 🇬𝑹𝑶𝑼𝑷█║', url=f'https://t.me/{BOT_USERNAME}?startgroup=true'),
    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(photo="https://telegra.ph/file/e6fd14982dad3f66563a4.jpg", caption=HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)
    await message.delete()


@Client.on_message(filters.command("help"))
async def show_help(client, message):
    buttons = [
        [
                InlineKeyboardButton('⚡𝕮𝖍𝖆𝖓𝖓𝖊𝖑⚡', url='https://t.me/ABOUT_ARVI'),
                InlineKeyboardButton('乂❤₲ⱤØɄ₱❤乂', url='https://t.me/world_wide_chattt')
                ],[
                InlineKeyboardButton('👸🇪🅻🅸👸', url='https://t.me/Eliana_072'),
                InlineKeyboardButton('👸🇦🆁🆅🅸👸', url='https://t.me/FOREVER_ANGEL_0')
                ],[
                InlineKeyboardButton('║█🇦𝑫𝑫 🇲𝑬 🇹𝑶 🇾𝑶𝑼𝑹 🇬𝑹𝑶𝑼𝑷█║', url=f'https://t.me/{BOT_USERNAME}?startgroup=true'),
       ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(photo="https://telegra.ph/file/e6fd14982dad3f66563a4.jpg", caption=HELP, reply_markup=reply_markup)
    await message.delete()
