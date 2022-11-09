import telebot
from telebot import types
import configure
import weather
import database
import datetime
import time
from threading import Thread
import schedule

bot = telebot.TeleBot(configure.config["token"])

urlKGD = "https://kgd.ru/pogoda/1-pogoda-v-kaliningrade"

diary = []

@bot.message_handler(commands = ["start"])
def start(message):
    global markup
    markup = types.ReplyKeyboardMarkup(one_time_keyboard = True, resize_keyboard = True)
    keyboard_weather = types.KeyboardButton(text = "Узнать погоду 🌧")
    keyboard_check_diary = types.KeyboardButton(text="Все записи 📃")
    keyboard_create_diary = types.KeyboardButton(text = "Добавить запись 📝")
    keyboard_delete_diary = types.KeyboardButton(text = "Удалить запись 📝")
    keyboard_check_diary_today = types.KeyboardButton(text = "Все записи на сегодня 📑")

    markup.add(keyboard_check_diary, keyboard_check_diary_today)
    markup.add(keyboard_create_diary, keyboard_delete_diary)
    markup.add(keyboard_weather)

    bot.send_message(message.chat.id, f"Привет {message.chat.first_name}!\n" , reply_markup = markup)

@bot.message_handler(content_types = "text")
def message_reply(message):
    if message.text == "Узнать погоду 🌧":
        weather.parse(urlKGD)
        bot.send_message(message.chat.id, f"Температура составляет: {weather.weather[0]['temp']}\n"
                                          f"Ветер: {weather.weather[0]['wind']}\n"
                                          f"Влажность: {weather.weather[0]['humidity']}\n"
                                          f"Давление: {weather.weather[0]['pressure']}\n"
                                          f"Облачность: {weather.weather[0]['cloudiness']}\n"
                                          f"Видимость: {weather.weather[0]['visibility']}")

    if message.text == "Добавить запись 📝":
        data_diary = bot.send_message(message.chat.id, "Введите дату записи")
        bot.register_next_step_handler(data_diary, add_data)

    if message.text == "Все записи 📃":
        database.cursor.execute("SELECT data, text FROM diary WHERE id = ?", (message.chat.id,))
        all_diary = database.cursor.fetchall()
        for i in range(len(all_diary)):
            bot.send_message(message.chat.id, f"Напоминание №{i+1}, дата {all_diary[i][0]}. \n{all_diary[i][1]}")

    if message.text == "Все записи на сегодня 📑":
        date = datetime.datetime.now().strftime('%d.%m.%Y')
        database.cursor.execute("SELECT data, text FROM diary WHERE id = ? AND data = ?", (message.chat.id, date))
        all_diary_today = database.cursor.fetchall()
        if all_diary_today:
            for i in range(len(all_diary_today)):
                bot.send_message(message.chat.id, f"Напоминание №{i + 1}. \n{all_diary_today[i][1]}")
        else:
            bot.send_message(message.chat.id, "На сегодня запланированных дел нет.")

    #if message.text == "Удалить запись 📝":
        #delete_data = bot.send_message(message.chat.id, "Укажите дату")
        #bot.register_next_step_handler(delete_data, choice_delete)
'''
def choice_delete(message):
    data_for_delete = message.text
    database.cursor.execute("SELECT text FROM diary WHERE id = ? and data = ?", (message.chat.id, data_for_delete))
    y = database.cursor.fetchall()
    bot.send_message(message.chat.id, "Напишите номер напоминания, которое Вы хотите удалить")
    for i in range(len(y)):
        row_for_delete = bot.send_message(message.chat.id, f"Напоминание №{i + 1}, {y[i][0]}")
    bot.register_next_step_handler(row_for_delete, delete)

def delete(data): # вызывается
    print(data.text)
    database.cursor.execute("DELETE FROM diary WHERE text = ?", (data.text,))
    database.con.commit()
'''
def add_data(message):
    global data
    data = message.text
    text_diary = bot.send_message(message.chat.id, "Введите текст записи")
    bot.register_next_step_handler(text_diary, add_text)

def add_text(message):
    text = message.text
    diary.clear()
    diary.append({
        "id": message.chat.id,
        "data": data,
        "text": text
    })
    bot.send_message(message.chat.id, "Запись успешно добавлена!")
    add_data_bd(diary)

def add_data_bd(diary):
    database.con.execute("INSERT INTO diary VALUES(?,?,?);", (int(diary[0]["id"]), diary[0]["data"], diary[0]["text"]))
    database.con.commit()

def remind():
    database.cursor.execute("SELECT data FROM diary")
    data_from_bd = database.cursor.fetchall()
    for i in range(len(data_from_bd)):
        if data_from_bd[i][0] == (datetime.datetime.now().strftime('%d.%m.%Y')):
            database.cursor.execute("SELECT id, text FROM diary WHERE data = ?",(datetime.datetime.now().strftime('%d.%m.%Y'),))
            x = database.cursor.fetchall()
        else:
            pass

    bot.send_message(x[0][0], "На сегодня запланировано:")

    for i in range(len(x)):
        bot.send_message(x[i][0], f"№{i+1}, {x[i][1]}")

def scheduler():
    schedule.every().day.at("23:15").do(remind)

    while True:
        schedule.run_pending()
        time.sleep(1) #86400 - сутки

t = Thread(target = scheduler)
t.start()

bot.polling(none_stop = True, interval = 0)
