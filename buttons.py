from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from youtube_search import YoutubeSearch
from config import (USERNAME)

class BTN:
    def send_result(text):
        a = YoutubeSearch(text,max_results=5).to_dict()
        keyboard = InlineKeyboardMarkup(row_width=1)
        ls = []
        for i in a:
            ls.append(InlineKeyboardButton(text=str(i['title']), callback_data=str('https://youtube.com'+i['url_suffix'])))
        return keyboard.add(*ls)
    def button(video_url,video_id):
        return InlineKeyboardMarkup(row_width=True,keyboard=[
            [
                InlineKeyboardButton("📹 Videoni ko'rish",url=video_url),    
            ],
            [
                InlineKeyboardButton("🏠",callback_data='home'),
                InlineKeyboardButton("⤴️ Ulashish",switch_inline_query=video_id),
                InlineKeyboardButton("❌",callback_data='delete'),
            ]
        ])
    def sharebot():
        return InlineKeyboardMarkup(row_width=True,keyboard=[
            [InlineKeyboardButton("Bo'tga o'tish",url=f"https://t.me/{USERNAME}")]
        ])
