from telebot import TeleBot
from config import TOKEN
from handlers import (start, texts, callbacks, inline_mode)

bot = TeleBot(TOKEN)

def handlers():
    bot.register_message_handler(
        callback=start,
        commands=['start'],
        chat_types=['private'],
        pass_bot=True
    )
    bot.register_message_handler(
        callback=texts,
        content_types=['text'],
        chat_types=['private'],
        pass_bot=True,
    )
    bot.register_callback_query_handler(
        callback=callbacks,
        func=lambda call: True,
        pass_bot=True,
    )
    bot.register_inline_handler(
        callback=inline_mode,
        func=lambda m: True,
        pass_bot=True,
    )


if __name__ == '__main__':
    handlers()
    bot.infinity_polling()
