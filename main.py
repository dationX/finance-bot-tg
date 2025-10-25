import telebot
from telebot import types

from config import *
from db_logic import *

bot = telebot.TeleBot(token=TOKEN)

@bot.message_handler(commands=['start'])
def start_command(message: types.Message):
    pass


if __name__ == "__main__":
    bd = DB()
    bd.create_db()
    bot.polling(non_stop=True)