import telebot;
import types;
import message_api;
bot = telebot.TeleBot('5987833282:AAGUbvHQDirtaO1GzNuENM83J0lp5XG6fcw');


@bot.message_handler(content_types=['text'])
def get_text_messages(message):


        if message.text == "/start":
            bot.send_message(message.from_user.id, "Привет выбери что тебе нравиться и напишы в чат:"
                                                   "Смотреть человек бензопила"
                                                   "Торговая площадка стим"
                                                   "Легко учить C++, "
                                                   "Привет")
        elif message.text == "/help":
            bot.send_message(message.from_user.id,
                             "Привет выбери что тебе нравиться и напишы в чат:"
                                                   "Смотреть человек бензопила, "
                                                   "Торговая площадка стим, "
                                                   "Легко учить C++, "
                                                   "Привет")
        else:
            bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

            if message.text == "Смотреть человек бензопила":
                bot.send_message(message.from_user.id, "https://animego.org/anime/chelovek-benzopila-2119")
            elif message.text == "/help":
                bot.send_message(message.from_user.id,
                                 "Привет выбери что тебе нравиться и напишы в чат:, "
                                 "Смотреть человек бензопила, "
                                 "Торговая площадка стим, "
                                 "Легко учить C++, "
                                 "Привет")

            else:
                bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
                if message.text == "Торговая площадка стим":
                    bot.send_message(message.from_user.id, "https://steamcommunity.com/market/")
                elif message.text == "/help":
                    bot.send_message(message.from_user.id,
                                     "Привет выбери что тебе нравиться и напишы в чат:, "
                                     "Смотреть человек бензопила, "
                                     "Торговая площадка стим, "
                                     "Легко учить C++, "
                                     "Привет")

                else:
                    bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
                    if message.text == "Легко учить C++":
                        bot.send_message(message.from_user.id, "https://leetcode.com/")
                        bot.send_message(message.from_user.id, "https://www.youtube.com/watch?v=1S00eVRkXp4&list=PLQKy767t2EsqUsOaY56MdNEYQVhzF31TK")
                    elif message.text == "/help":
                        bot.send_message(message.from_user.id,
                                         "Привет выбери что тебе нравиться и напишы в чат:, "
                                         "Смотреть человек бензопила, "
                                         "Торговая площадка стим, "
                                         "Легко учить C++, "
                                         "Привет")

                    else:
                        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
                        if message.text == "Привет":
                            bot.send_message(message.from_user.id, "Поддержать: https://donatello.to/mar1s")
                            bot.send_message(message.from_user.id, "Не люблю кнопки! Мне 12 и кристалик, спамит текстом /help")
                            bot.send_message(message.from_user.id,  "Что бы написали опять и узнали еще что  можно написать и получить ответ")
                        elif message.text == "/help":
                            bot.send_message(message.from_user.id,
                                             "Привет выбери что тебе нравиться и напишы в чат:, "
                                             "Смотреть человек бензопила, "
                                             "Торговая площадка стим, "
                                             "Легко учить C++, "
                                             "Привет")

                        else:
                            bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
bot.polling(none_stop=True)
