import telebot;
bot = telebot.TeleBot('5987833282:AAGUbvHQDirtaO1GzNuENM83J0lp5XG6fcw');


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет написал этого бота Марис")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши Привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
        bot.polling(none_stop=True, interval=0)
