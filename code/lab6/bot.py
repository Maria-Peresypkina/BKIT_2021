import telebot
from telebot import types
import config
import dbworker

# Создание бота
bot = telebot.TeleBot(config.TOKEN)


# Начало диалога
@bot.message_handler(commands=['start'])
def cmd_start(message):
    bot.send_message(message.chat.id, "Привет! Я собираю данные про спорт!")
    dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.S_ENTER_NAME.value)
    bot.send_message(message.chat.id, 'Как вас зовут?')


# По команде /reset будем сбрасывать состояния, возвращаясь к началу диалога
@bot.message_handler(commands=['reset'])
def cmd_reset(message):
    bot.send_message(message.chat.id, 'Сбрасываем результаты предыдущего ввода.')
    dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.S_ENTER_NAME.value)
    bot.send_message(message.chat.id, 'Введите первое число')


# Обработка первого числа
@bot.message_handler(func=lambda message: dbworker.get(
    dbworker.make_key(message.chat.id, config.CURRENT_STATE)) == config.States.S_ENTER_NAME.value)
def user_name(message):
        # Состояние не изменяется, выводится сообщение об ошибке
        bot.send_message(message.chat.id, "Отличное имя, запомню! Теперь укажи, пожалуйста, свой возраст.")
        dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.S_ENTER_AGE.value)
        # Сохраняем первое число
   #     dbworker.set(dbworker.make_key(message.chat.id, config.States.STATE_FIRST_NUM.value), text)
    #    bot.send_message(message.chat.id, 'Введите второе число')


# Обработка второго числа
@bot.message_handler(func=lambda message: dbworker.get(
    dbworker.make_key(message.chat.id, config.CURRENT_STATE)) == config.States.S_ENTER_AGE.value)
def user_age(message):

    # А вот тут сделаем проверку
    if not message.text.isdigit():
        # Состояние не меняем, поэтому только выводим сообщение об ошибке и ждём дальше
        bot.send_message(message.chat.id, "Что-то не так, попробуй ещё раз!")
        return
    # На данном этапе мы уверены, что message.text можно преобразовать в число, поэтому ничем не рискуем
    if int(message.text) < 5 or int(message.text) > 100:
        bot.send_message(message.chat.id, "Какой-то странный возраст. Не верю! Отвечай честно.")
        return
    else:
        # Возраст введён корректно, можно идти дальше
        bot.send_message(message.chat.id, "Когда-то и мне было столько лет...эх... Впрочем, не будем отвлекаться. "
                                          "Отправь мне какую-нибудь фотографию.")
        dbworker.set_state(message.chat.id, config.States.S_SEND_PIC.value)

    text = message.text
    if not text.isdigit():
        # Состояние не изменяется, выводится сообщение об ошибке
        bot.send_message(message.chat.id, 'Пожалуйста введите число!')
        return
        # На данном этапе мы уверены, что message.text можно преобразовать в число, поэтому ничем не рискуем
    if int(message.text) < 5 or int(message.text) > 100:
        bot.send_message(message.chat.id, "Какой-то странный возраст. Не верю! Отвечай честно.")
        return
    else:
        bot.send_message(message.chat.id, "Когда-то и мне было столько лет...эх... Впрочем, не будем отвлекаться. "
                                          "Отправь мне какую-нибудь фотографию.")
        # Меняем текущее состояние
 #       dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.STATE_OPERATION.value)
        # Сохраняем первое число
        dbworker.set(dbworker.make_key(message.chat.id, config.States.S_SEND_PIC.value),
  #      markup = types.ReplyKeyboardMarkup(row_width=2)
 #       itembtn1 = types.KeyboardButton('+')
#        itembtn2 = types.KeyboardButton('*')
 #       markup.add(itembtn1, itembtn2)
 #       bot.send_message(message.chat.id, 'Выберите пожалуйста действие', reply_markup=markup)


# Выбор действия
'''''@bot.message_handler(func=lambda message: dbworker.get(
    dbworker.make_key(message.chat.id, config.CURRENT_STATE)) == config.States.STATE_OPERATION.value)
def operation(message):
    # Текущее действие
    op = message.text
    # Читаем операнды из базы данных
    v1 = dbworker.get(dbworker.make_key(message.chat.id, config.States.STATE_FIRST_NUM.value))
    v2 = dbworker.get(dbworker.make_key(message.chat.id, config.States.STATE_SECOND_NUM.value))
    # Выполняем действие
    fv1 = float(v1)
    fv2 = float(v2)
    res = 0
    if op == '+':
        res = fv1 + fv2
    elif op == '*':
        res = fv1 * fv2
    # Выводим результат
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.chat.id, f'Результат: {v1}{op}{v2}={str(res)}', reply_markup=markup)
    # Меняем текущее состояние
    dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.STATE_FIRST_NUM.value)
    # Выводим сообщение
    bot.send_message(message.chat.id, 'Введите первое число')
    '''''

@bot.message_handler(content_types=["photo"],
                     func=lambda message: dbworker.get(message.chat.id) == config.States.S_SEND_PIC.value)
def user_sending_photo(message):
    # То, что это фотография, мы уже проверили в хэндлере, никаких дополнительных действий не нужно.
    bot.send_message(message.chat.id, "Отлично! Больше от тебя ничего не требуется. Если захочешь пообщаться снова - "
                     "отправь команду /start.")
    dbworker.set(message.chat.id, config.States.S_START.value)

if __name__ == '__main__':
    bot.infinity_polling()

