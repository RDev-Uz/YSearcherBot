from telebot import TeleBot
from telebot.types import (Message, CallbackQuery, InlineQuery, 
                            InlineQueryResultArticle,InputTextMessageContent)
from youtube_search import YoutubeSearch
from buttons import BTN
from config import (USERNAME, SHARE_TEXT)

def start(m: Message, bot: TeleBot):
    bot.send_message(m.chat.id,f"""Assalomu Alaykum <a href={m.chat.id}>{m.from_user.first_name}</a>!
    
🔎 Ushbu bot sizga youtube.com'dan videolarni qidirishda yordam beradi!

Buning uchun botga qidirish uchun matn yuborsangiz kifoya.""",parse_mode='HTML')

def texts(m: Message,bot: TeleBot):
    try:
        bot.send_message(m.chat.id,"Qidiruv natijalari:",reply_markup=BTN.send_result(m.text))
    except:
        bot.send_message(m.chat.id,"Afsuski topilmadi!")       

def info(url):
    res = YoutubeSearch(url,max_results=1).to_dict()[0]
    try:
        return [res['thumbnails'][1],res['title'],res['views'][:-5],res['channel'],res['duration'],res['id']]
    except:
        return [res['thumbnails'][0],res['title'],res['views'][:-5],res['channel'],res['duration'],res['id']]   

def callbacks(call: CallbackQuery, bot: TeleBot):
    if call.data:
        info_ = info(call.data)
        bot.delete_message(call.message.chat.id,call.message.message_id)
        bot.send_photo(call.message.chat.id,photo=info_[0],
        caption=f"📹 <b>{info_[1]}</b>\n\n©️ Kanal nomi: {info_[3]}\n⏳ Davomiyligi: {info_[4]} daqiqa\n👁 Ko'rishlar soni: {info_[2]}ta\n\n🔗 <code>{call.data}</code>\n\n👉 @{USERNAME}",
        parse_mode='HTML',
        reply_markup=BTN.button(call.data,info_[-1]))

def share_bot() -> None:
    return InlineQueryResultArticle(id='1',
    title="🔗 Botni ulashish",
    description="Botimizni yaqinlaringiz bilan baham ko'ring!",
    input_message_content=InputTextMessageContent(SHARE_TEXT), 
    thumb_url="https://rahmatulloh.tk/share.png",
    reply_markup=BTN.sharebot())

def inline_mode(m: InlineQuery, bot: TeleBot):
    if m.query:
        re = YoutubeSearch(f'https://youtube.com/watch?v={m.query}',max_results=1).to_dict()
        if (re[0]['id'] == m.query):
            info_ = info(f'https://youtube.com/watch?v={m.query}')
            result = InlineQueryResultArticle(
                id='1',
                title=info_[1],
                input_message_content=InputTextMessageContent(
                    f"📹 <b>{info_[1]}</b>\n\n©️ Kanal nomi: {info_[3]}\n⏳ Davomiyligi: {info_[4]} daqiqa\n👁 Ko'rishlar soni: {info_[2]}ta\n\n🔗 <code>https://youtube.com/watch?v={m.query}</code>\n\n👉 @{USERNAME}",
                    parse_mode='HTML'),
                thumb_url=info_[0],
                description="Ulashish uchun bosing!",
                reply_markup=BTN.button(f'https://youtube.com/watch?v={m.query}',m.query)
            )
            bot.answer_inline_query(m.id,[result],cache_time=1)
        else:
            bot.answer_inline_query(m.id,results=[share_bot()],switch_pm_text="Bo'tga o'tish",switch_pm_parameter='must_click')
    else:
        bot.answer_inline_query(m.id,results=[share_bot()],switch_pm_text="Bo'tga o'tish",switch_pm_parameter="must_click")

