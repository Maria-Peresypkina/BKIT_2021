import telebot
import config
import dbworker

bot = telebot.TeleBot(config.token)

# Начало диалога
@bot.message_handler(commands=["start"])
def cmd_start(message):
    bot.send_message(message.chat.id, "Привет! Как тебя зовут?")
    dbworker.set_state(message.chat.id, config.States.S_ENTER_NAME.value)

# По команде /reset будем сбрасывать состояния, возвращаясь к началу диалога
@bot.message_handler(commands=["reset"])
def cmd_reset(message):
    bot.send_message(message.chat.id, "Хорошо, начнём заново. Как тебя зовут?")
    dbworker.set_state(message.chat.id, config.States.S_ENTER_NAME.value)

@bot.message_handler(
    func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_ENTER_NAME.value)
def user_entering_name(message):
     # В случае с именем не будем ничего проверять, пусть хоть "25671", хоть Евкакий
    bot.send_message(message.chat.id, "Отличное имя! Теперь укажи, пожалуйста, сколько тебе лет.")
    dbworker.set_state(message.chat.id, config.States.S_ENTER_AGE.value)

@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_ENTER_AGE.value)
def user_entering_age(message):
    # А вот тут сделаем проверку
    if not message.text.isdigit():
        # Состояние не меняем, поэтому только выводим сообщение об ошибке и ждём дальше
        bot.send_message(message.chat.id, "Что-то не так, попробуй ещё раз!")
        return
    # На данном этапе мы уверены, что message.text можно преобразовать в число, поэтому ничем не рискуем
    if int(message.text) < 5 or int(message.text) > 100:
        bot.send_message(message.chat.id, "Вы указали странный возраст. Напишите его ещё раз.")
        return
    else:
        # Возраст введён корректно, можно идти дальше
        bot.send_message(message.chat.id, "Прекрасный возраст! "
                                          "Отправь мне какую-нибудь фотографию.")
        dbworker.set_state(message.chat.id, config.States.S_SEND_PIC.value)

@bot.message_handler(content_types=["photo"],
                     func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_SEND_PIC.value)
def user_sending_photo(message):
    # То, что это фотография, мы уже проверили в хэндлере, никаких дополнительных действий не нужно.
    bot.send_message(message.chat.id, "Супер! Больше от тебя ничего не требуется. Если захочешь пообщаться снова - "
                     "отправь команду /start.")
    dbworker.set_state(message.chat.id, config.States.S_START.value)

if __name__ == '__main__':
    bot.infinity_polling()

