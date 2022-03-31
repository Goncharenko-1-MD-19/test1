# Вариант 1 - самый простой чат бот, просто отзывается

import telebot  # pyTelegramBotAPI	4.3.1
from telebot import types
import requests
import bs4
import json
#from lxml import html
from bs4 import BeautifulSoup

bot = telebot.TeleBot('5283884291:AAFnYV4e2epLWZ5uMbw90RDVOkNsK3I5yLQ')  # Создаем экземпляр бота @Ivanov_Ivan_1MD19_bot

# -----------------------------------------------------------------------
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(message, res=False):
    chat_id = message.chat.id

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Главное меню")
    btn2 = types.KeyboardButton("❓ Помощь")
    markup.add(btn1, btn2)
    bot.send_message(chat_id,
                     text="Привет, {0.first_name}! Я тестовый бот для курса программирования на языке ПаЙтон".format(
                         message.from_user))


# -----------------------------------------------------------------------
#Получение сообщений от юзера
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    chat_id = message.chat.id
    ms_text = message.text
    if ms_text == "Главное меню" or ms_text == "👋 Главное меню" or ms_text == "Вернуться в главное меню":  # ..........
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Развлечения")
        btn2 = types.KeyboardButton("WEB-камера")
        btn3 = types.KeyboardButton("Управление")
        back = types.KeyboardButton("Помощь")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(chat_id, text="Вы в главном меню", reply_markup=markup)

    elif ms_text == "Развлечения":  # ..................................................................................
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Прислать собаку")
        btn2 = types.KeyboardButton("Прислать анекдот")
        btn3 = types.KeyboardButton("Покажи себя (мб 18+)")
        btn4 = types.KeyboardButton('Курс доллара')
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, btn4, back)
        bot.send_message(chat_id, text="Развлечения", reply_markup=markup)

    elif ms_text == "/dog" or ms_text == "Прислать собаку":  # .........................................................
        url = 'https://randomfox.ca/floof/'
        response = requests.get(url).json()
        urldog = response['image']
        bot.send_photo(chat_id, photo = urldog, caption="Не будет собаки, будет лиса \U0001F61C")
    elif ms_text == "Прислать анекдот":  # .............................................................................
        url = 'https://www.anekdot.ru/random/anekdot/'
        zap = requests.get(url)
        soup = bs4.BeautifulSoup(zap.text, 'html.parser')
        result = soup.select_one('currency-table__large-text')
        res = result.getText().strip()
        bot.send_message(chat_id, text=res)

    elif ms_text == "Курс доллара":  # .............................................................................
        url = 'https://www.banki.ru/products/currency/usd/'
        zap = requests.get(url)
        soup = bs4.BeautifulSoup(zap.text, 'html.parser')
        print(soup)
        #result = soup.select_one('.text')
        #res = result.getText().strip()
        #bot.send_message(chat_id, text=res)

    elif ms_text == "WEB-камера":
        bot.send_message(chat_id, text="еще не готово...")

    elif ms_text == "Управление":  # ...................................................................................
        bot.send_message(chat_id, text="еще не готово...")



    elif ms_text == "Помощь" or ms_text == "/help":  # .................................................................
        bot.send_message(chat_id, "Автор: Дмитрий Михайленко")
        key1 = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="Напишите автору", url="https://t.me/God_Pain")
        key1.add(btn1)
        img = open('hitryy.jpg', 'rb')
        bot.send_photo(message.chat.id, img, reply_markup=key1)

    else:  # ...........................................................................................................
        bot.send_message(chat_id, text="Я тебя слышу!!! Ваше сообщение: " + ms_text)


# -----------------------------------------------------------------------
bot.polling(none_stop=True, interval=0) # Запускаем бота

print()
