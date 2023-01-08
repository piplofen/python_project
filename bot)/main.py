import telebot
from telebot import types
import cfg
import time

bot = telebot.TeleBot(cfg.token)

@bot.message_handler(commands=["start"])
def start(message):
    global keyboard
    if str(message.chat.id) == str(cfg.group):
        bot.send_message(message.chat.id, f"Для тебя ({message.from_user.first_name}) функционал отсутствует 😝")
    elif str(message.chat.id) != str(cfg.group):
        keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        keyboard_info = types.KeyboardButton(text="Узнать информацию 📊")
        keyboard_add = types.KeyboardButton(text="Создать объявление 📝")

        keyboard.add(keyboard_info)
        keyboard.add(keyboard_add)

        bot.send_message(message.chat.id, f"Привет {message.from_user.first_name}!\nЯ ботяра нулёвая", reply_markup=keyboard)

@bot.message_handler(content_types="text")
def message_reply(message):
    if message.text == "Узнать информацию 📊":
        if bot.get_chat_members_count(cfg.group) % 10 == 1:
            bot.send_message(message.chat.id, f"========={bot.get_chat(cfg.group).title}=========\n"
                                              f"В группе находится {bot.get_chat_members_count(cfg.group)} человек\n", reply_markup=keyboard)
        else:
            bot.send_message(message.chat.id, f"========={bot.get_chat(cfg.group).title}=========\n"
                                              f"В группе находится {bot.get_chat_members_count(cfg.group)} человека\n"
                                              f"{bot.get_chat(cfg.group)}", reply_markup=keyboard)

    elif message.text == "Создать объявление 📝":
        bot.send_message(message.chat.id, "Создаем объявление, подождите секунду", reply_markup=keyboard)
        time.sleep(1)
        textAnnouncement = bot.send_message(message.chat.id, "Введите текст объявления")
        bot.register_next_step_handler(textAnnouncement, add_textAnnouncement)

    elif message.text == "Да":
        bot.send_message(message.chat.id, "хых", reply_markup=keyboard)

    elif message.text == "Нет":
        bot.send_message(message.chat.id, "ЫЫЫЫ", reply_markup=keyboard)

def add_textAnnouncement(message):
    text = message.text
    bot.send_message(message.chat.id, f"Ваше сообщение: ⬇\n{text}", reply_markup=keyboard)
    keyboardStep2 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    keyboardStep2_Accept = types.KeyboardButton(text="Да")
    keyboardStep2_NotAccept = types.KeyboardButton(text="Нет")

    keyboardStep2.add(keyboardStep2_Accept, keyboardStep2_NotAccept)

    bot.send_message(message.chat.id, "Выкладываем это объявление?", reply_markup=keyboardStep2)

# @bot.message_handler(content_types="text")
# def message_reply(message):
#     if message.text == "Да":
#         bot.send_message(message.chat.id, f"Щя выложу")
#
#     elif message.text == "Нет":
#         bot.send_message(message.chat.id, "Понял")


bot.polling(none_stop = True, interval = 0)