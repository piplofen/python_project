import telebot, sqlite3, datetime, random
from telebot import types

try:
    conn = sqlite3.connect("database.db", check_same_thread=False)
    cur = conn.cursor()
    print(f"{datetime.datetime.now()} Подключение к базе данных прошло успешно!")

except sqlite3.Error as e:
    print(f"{datetime.datetime.now()} Произошла ошибка '{e}'")

bot = telebot.TeleBot("5791423620:AAEUGOqvRCWd1NP_5md1zBpOWhdBu0pEcW8")

#1576279249 Алена Анатольевна
#432965307 я

@bot.message_handler(commands = ["start"])
def start(message):
    user_id = message.from_user.id
    if (user_id == 1576279249) or (user_id == 432965307):
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
        keyboard_choice = types.KeyboardButton(text="Выбрать свидание 😘")
        markup.add(keyboard_choice)

        if user_id == 1576279249:
            bot.send_message(message.chat.id, f"Привет моя хорошая))) 🥰\n", reply_markup=markup)
        elif user_id == 432965307:
            bot.send_message(message.chat.id, f"Салам Алейкум старичок 😎\n", reply_markup=markup)

    else:
        bot.send_message(message.chat.id, "Тебе нельзя пользоваться этим ботом) 😜")


@bot.message_handler(content_types = "text")
def message_reply(message):
    if message.text == "Выбрать свидание 😘":
        id = random.randint(1, 10)
        cur.execute(f"select text from options where id = {id}")
        res = cur.fetchall()
        bot.send_message(message.chat.id, res)
    else:
        bot.send_message(message.chat.id, "Я пока что не знаю такой команды, но ты можешь написать моему создателю и он ее добавит)")

bot.polling(none_stop = True, interval = 0)