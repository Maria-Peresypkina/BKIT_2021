import telebot
from telebot import apihelper


token = '5070161387:AAFw8hwrXu2AR7vw_VARR17KSa7R5XIVWro'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Привет', 'Пока')
    bot.send_message(message.chat.id, 'Привет!', reply_markup=keyboard)

@bot.message_handler(commands=['test'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='21 марта - 20 апреля', callback_data=1))
    markup.add(telebot.types.InlineKeyboardButton(text='21 апреля - 21 мая', callback_data=2))
    markup.add(telebot.types.InlineKeyboardButton(text='22 мая - 21 июня', callback_data=3))
    markup.add(telebot.types.InlineKeyboardButton(text='22 июня - 22 июля', callback_data=4))
    markup.add(telebot.types.InlineKeyboardButton(text='23 июля - 23 августа', callback_data=5))
    markup.add(telebot.types.InlineKeyboardButton(text='24 августа - 23 сентября', callback_data=6))
    markup.add(telebot.types.InlineKeyboardButton(text='24 сентября - 23 октября', callback_data=7))
    markup.add(telebot.types.InlineKeyboardButton(text='24 октября - 22 ноября', callback_data=8))
    markup.add(telebot.types.InlineKeyboardButton(text='23 ноября - 22 декабря', callback_data=9))
    markup.add(telebot.types.InlineKeyboardButton(text='23 декабря - 20 января', callback_data=10))
    markup.add(telebot.types.InlineKeyboardButton(text='21 января - 19 февраля', callback_data=11))
    markup.add(telebot.types.InlineKeyboardButton(text='20 февраля - 20 марта', callback_data=12))
    bot.send_message(message.chat.id, text="Когда у вас день рождения?", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Ещё раз привет! Давай определим твой знак зодиака!')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Пока!')

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):

    bot.answer_callback_query(callback_query_id=call.id, text='Спасибо за ответ!')
    answer = ''
    if call.data == '1':
        answer = 'Вы - Овен!'
    elif call.data == '2':
        answer = 'Вы - Телец!'
    elif call.data == '3':
        answer = 'Вы - Близнецы!'
    elif call.data == '4':
        answer = 'Вы - Рак!'
    elif call.data == '5':
        answer = 'Вы - Лев!'
    elif call.data == '6':
        answer = 'Вы - Дева!'
    elif call.data == '7':
        answer = 'Вы - Весы!'
    elif call.data == '8':
        answer = 'Вы - Скорпион!'
    elif call.data == '9':
        answer = 'Вы - Стрелец!'
    elif call.data == '10':
        answer = 'Вы - Козерог!'
    elif call.data == '11':
        answer = 'Вы - Водолей!'
    elif call.data == '12':
        answer = 'Вы - Рыбы!'


    bot.send_message(call.message.chat.id, answer)
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

bot.polling()