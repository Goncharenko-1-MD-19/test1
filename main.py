import json
from gettext import find
from io import BytesIO

import telebot  # pyTelegramBotAPI 4.3.1
from telebot import types
import requests
import bs4   #beautifulsoup4
import BotGames  # бот-игры, файл BotGames.py
from menuBot import Menu  # в этом модуле есть код, создающий экземпляры классов описывающих моё меню
import DZ

bot = telebot.TeleBot('5136955618:AAF5wY837jw4MdPTrJFKctR4YgknjiWmox8')
game21 = None

@bot.message_handler(commands="start")
def command(message):
   txt_message = f"Привет, {message.from_user.first_name}! Я тестовый бот для курса программирования на языке Python"
   bot.send_message(message.chat.id, text=txt_message, reply_markup=Menu.getMenu("Главное меню").markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
   global game21

   chat_id = message.chat.id
   ms_text = message.text

   result = goto_menu(chat_id, ms_text)
   if result == True:
       return

   if Menu.cur_menu != None and ms_text in Menu.cur_menu.buttons:

       if ms_text == "Помощь":
           send_help(chat_id)

       elif ms_text == "/dog" or ms_text == "Прислать собаку":
           url = 'https://randomfox.ca/floof/'
           response = requests.get(url).json()
           urldog = response['image']
           bot.send_photo(chat_id, photo=urldog, caption="Не будет собаки, будет лиса \U0001F61C")

       elif ms_text == "Напишите":
             bot.send_message(message.chat.id,"Введите текст на английском языке")



       elif ms_text == "Карту!":
           if game21 == None:
               goto_menu(chat_id, "Выход")
               return

           text_game = game21.get_cards(1)
           bot.send_media_group(chat_id, media=getMediaCards(game21))
           bot.send_message(chat_id, text=text_game)

           if game21.status != None:
               goto_menu(chat_id, "Выход")
               return

       elif ms_text == "Стоп!":
           game21 = None
           goto_menu(chat_id, "Выход")
           return

       elif ms_text == "Задание-1":
           DZ.dz1(bot, chat_id)

       elif ms_text == "Задание-2":
           DZ.dz2(bot, chat_id)

       elif ms_text == "Задание-3":
           DZ.dz3(bot, chat_id)

       elif ms_text == "Задание-4":
           DZ.dz4(bot, chat_id)

       elif ms_text == "Задание-5":
           DZ.dz5(bot, chat_id)

       elif ms_text == "Задание-6":
           DZ.dz6(bot, chat_id)

   else:  # ...........................................................................................................
       bot.send_message(chat_id, text="Мне жаль, я не понимаю вашу команду: " + ms_text)
       goto_menu(chat_id, "Главное меню")
# -----------------------------------------------------------------------
def goto_menu(chat_id, name_menu):


   if name_menu == "Выход" and Menu.cur_menu != None and Menu.cur_menu.parent != None:
       target_menu = Menu.getMenu(Menu.cur_menu.parent.name)
   else:
       target_menu = Menu.getMenu(name_menu)

   if target_menu != None:
       bot.send_message(chat_id, text=target_menu.name, reply_markup=target_menu.markup)


       if target_menu.name == "Игра в 21":
           global game21
           game21 = BotGames.Game21()
           text_game = game21.get_cards(2)
           bot.send_media_group(chat_id, media=getMediaCards(game21))
           bot.send_message(chat_id, text=text_game)

       return True
   else:
       return False

def getMediaCards(game21):
   medias = []
   for url in game21.arr_cards_URL:
       medias.append(types.InputMediaPhoto(url))
   return medias


def send_help(chat_id):
   global bot
   bot.send_message(chat_id, "Автор: Гончаренко Глеб")
   key1 = types.InlineKeyboardMarkup()
   btn1 = types.InlineKeyboardButton(text="Напишите автору", url="https://t.me/gleb242")
   key1.add(btn1)
   img = open('gleb.jpg', 'rb')
   bot.send_photo(chat_id, img, reply_markup=key1)

# -----------------------------------------------------------------------
def get_anekdot():
   array_anekdots = []
   req_anek = requests.get('http://anekdotme.ru/random')
   soup = bs4.BeautifulSoup(req_anek.text, "html.parser")
   result_find = soup.select('.anekdot_text')
   for result in result_find:
       array_anekdots.append(result.getText().strip())
   return array_anekdots[0]

def get_send_message():



def get_dogURL():
   contents = requests.get('https://saltmag.ru/lifestyle/fun/6373-luchshie-memy-s-kotami/').json()
   return contents['url']



bot.polling(none_stop=True, interval=0)  # Запускаем бота

print()