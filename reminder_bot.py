import telebot
import os
from dotenv import load_dotenv

##load_dotenv()
##BOT_TOKEN = os.getenv("6902877477:AAExDyJA6Z8QBH0PloXnVMo-VitUurjZ5MI")

bot = telebot.TeleBot("6902877477:AAExDyJA6Z8QBH0PloXnVMo-VitUurjZ5MI")

# Handler for '/start' command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! I'm your bot, ready to assist you.")

# Handler for '/hello' command
@bot.message_handler(commands=['hello'])
def greet_user(message):
    bot.reply_to(message, "Hello there! How can I help you today?")

# Handler for any other message
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# Start the bot
bot.infinity_polling()
