import telebot
import constants
# import time
from telebot.types import Message
bot = telebot.TeleBot(constants.token)

print(bot.get_me())


def log(message, answer):
    print("\n -------")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2}) \n Текст - {3}".format(message.from_user.first_name,
                                                                   message.from_user.last_name,
                                                                   str(message.from_user.id),
                                                                   message.text))
    print(answer)


"""
@bot.message_handler(commands=["start"])
def handle_text(message):
    bot.send_message(message.chat.id, "Добро пожаловать, огрызок")
@bot.message_handler(commands=["help"])
def handle_text(message):
    bot.send_message(message.chat.id, "Бог поможет, чмо")
@bot.message_handler(commands=["settings"])
def handle_text(message):
    bot.send_message(message.chat.id, "Очко себе настрой, петух")


@bot.message_handler(content_types=["text"])
def handle_text(message):
    answer = "ебаный поровоз иди ты уже нахуй"
    if message.text == "a":
        answer = "b"
        bot.send_message(message.chat.id, answer)
        log(message, answer)
    elif message.text == "b":
        answer = "a"
        bot.send_message(message.chat.id, answer)
        log(message, answer)
    else:
        bot.send_message(message.chat.id, answer)
        log(message, answer)
"""


@bot.message_handler(commands=["start", "help", "settings"])
def command_handler(message: Message):
    bot.reply_to(message, "Сдуйся, опездол")


@bot.message_handler(content_types=["text"])
@bot.edited_message_handler(content_types=["text"])
def echo_digits(message: Message):
    text = message.text.lower()
    if "фергус" in text:
        if str(message.from_user.id) == "295674037":
            bot.reply_to(message, "Внемлю вам, господин")
            return
        else:
            bot.reply_to(message, "Сдуйся, дерьмодемон. Админ занят важными делами")


@bot.message_handler(content_types=["sticker"])
def echo_digits(message: Message):
        if str(message.from_user.id) == "295674037":
            bot.reply_to(message, "Блин-блинский, крутой стикер, да и подметил ты ловко. Вот бы все так делали")
        else:
            bot.reply_to(message, "Господи, ну ты и хуебес. За стикеры эти молодёжные-дерьмосраные ты у меня такого члену получишь")


@bot.message_handler(content_types=["photo"])
def echo_digits(message: Message):
        if str(message.from_user.id) == "295674037":
            bot.reply_to(message, "Великолепный мэм, пиздец. В жизни так не ржал. Я хочу от тебя детей")
        else:
            bot.reply_to(message, "Ну ты и дерьмо отправил, додик. Хуёвый Мэм, бан, дисреспект")


"""
while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)
"""


if __name__ == '__main__':
    bot.polling(none_stop=True)
