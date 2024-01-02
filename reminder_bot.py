import telebot
import os
from dotenv import load_dotenv

class TelegramReminderBot:
    def __init__(self,BOT_TOKEN):
        self.bot = telebot.TeleBot(BOT_TOKEN)
        self.setup_handlers()
    
    def setup_handlers(self):
        @self.bot.message_handler(commands=['start'])
        def send_welcome(message):
            self.bot.reply_to(message,"Welcome! I'm your bot, ready to assist you.")
        
        @self.bot.message_handler(commands=['hello'])
        def greet_user(message):
            self.bot.reply_to(message,"Hello there! How can I help you today?")
        
        @self.bot.message_handler(func=lambda message: True)
        def echo_all(message):
            self.bot.reply_to(message, message.text)

    def start(self):
        self.bot.infinity_polling()

if __name__ == '__main__':
    load_dotenv()
    BOT_TOKEN = os.getenv("BOT_TOKEN")

    if BOT_TOKEN:
        reminder_bot = TelegramReminderBot(BOT_TOKEN)
        reminder_bot.start()
    else:
        raise Exception('Bot token is not defined')

