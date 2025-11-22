import telebot
from telebot import types
import datetime
import os

from config import *
from db_logic import *
from funcs import *

bot = telebot.TeleBot(token=TOKEN)


@bot.message_handler(commands=['start'])
def start_command(message: types.Message):
    db.add_user(message.from_user.id)
    bot.send_message(message.chat.id, "Привет!", parse_mode='Markdown')


@bot.message_handler(commands=['add_money'])
def add_money(message: types.Message):
    date_time = datetime.datetime.now()
    str_date = date_time.strftime("%Y-%m-%d %H:%M:%S")

    user_text = message.text.split(' ')

    money = user_text[1]

    category = ""
    for text in user_text[2:]:
        category += f"{text} "

    user_id = message.from_user.id

    db.add_money(user_id, money, category, str_date)


@bot.message_handler(commands=['remove_money'])
def remove_money(message: types.Message):
    """Обнуление кошелька пользователя"""
    db.reset(message.from_user.id)


@bot.message_handler(commands=['info'])
def info(message: types.Message):
    user_id = message.from_user.id
    money = db.info_money(user_id)
    db_data_fr = db.info_money_category(user_id)

    bot.send_message(message.chat.id, f"_Ваш баланс составляет_ *{money[0]}*", parse_mode='markdown')

    create_table_money(user_id, db_data_fr)

    with open(f"{user_id}_table_mon_opr.png", 'rb') as file:
        image = file
        bot.send_photo(message.chat.id, image, "*Ваш список операций:*", parse_mode='markdown')
        os.remove(f"{user_id}_table_mon_opr.png")

if __name__ == "__main__":
    db = DB()
    db.create_db()
    bot.polling(non_stop=True)