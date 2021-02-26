import config

import telebot

from telebot import types

token = 'config.TGToken'
bot = telebot.TeleBot(token)
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Привет', '/help')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start. Как тебя зовут?', reply_markup=keyboard1)

@bot.message_handler(content_types=['text', 'document', 'audio'])
def get_text_message(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет, чем я могу помочь?')
    elif message.text == '/help':
        bot.send_message(message.from_user.id, 'Напиши привет')
    else:
        bot.send_message(message.from_user.id, 'Я тебя не понимаю, напиши /help.')

name = ''
surname = ''
age = 0

@bot.message_handler(commands=['reg'])
def start_message(message):
    bot.send_message(message.chat.id,'Давай я узнаю кто ты')

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, 'Как тебя зовут?')
        bot.register_next_step_handler(message, get_name) #слудющий шаг - функция
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg')
def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname)
def get_surname(message):
    global surnamz
    surname = message.text
    bot.send_message(message.from_user.id, 'Сколько тебе лет')
    bot.register_next_step_handler(message, get_age)
def ger_age(message):
    global  age
    while age == 0: #проверяем, что возраст изменился
        try:
            age = int(message.text) #проверяем, что возраст веден корректно
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами пожалуйста')
        keyboard2 = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text = 'Да', callback_data = 'yes')
        keyboard2.add(key_yes); #добавляем кнопку в клавиатуру
        key_no = types.InlineKeyboardButton(text = 'Нет', callback_data= 'no')
        keyboard2.add(key_no)
        question = 'Тебе ' + str(age) + ' лет, тебя зовут ' + name + ' ' + surname + '?'

        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard2)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes": #call.data это callback_data, которую мы указали при объявлении кнопки
        ...
        bot.send_message(call.message.chat.id, 'Запомню :)'); #код сохранения данных, или их обработки
    elif call.data == "no": #переспрашиваем
        ...
bot.polling(none_stop=True, interval=0)


