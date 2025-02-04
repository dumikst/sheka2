# main.py
import telebot
from config import TOKEN
from handlers import setup_handlers

def main():
    bot = 8133521404:AAHQ8tcxjdCCVoid_jVvJlTWbx3RcFJC_YQ

    user_messages = {}
    user_message_ids = {}

    setup_handlers(bot, user_messages, user_message_ids)

    # Запуск бота
    bot.polling(none_stop=True)

if __name__ == "__main__":
    main()
