import pyowm
import telebot


bot = telebot.TeleBot("407153571:AAF1HGMTb92U4ERzPj2dRfUh5vIeVr8GbUE")
user_markup = telebot.types.ReplyKeyboardMarkup(True, False)

"""
print ("В городе " + city + "," + " " + "сейчас температура: " + str (temperatura) + " " + "по Цельсию." )
print (  "Направление и скорость ветра" + " " + str (veter)  )
print ("Влажность в городе" + " " + city + " " + str (vlash) )
print ( detalstat + "\n")
"""
city_add = 0
def log(message):
    print("\n-----")
    from datetime import datetime
    print(str(datetime.now()))
    print("Сообщение от {0} {1}. (id = {2}) \n Text: '{3}'".format(message.from_user.first_name,
                                                             message.from_user.last_name,
                                                             str(message.from_user.id),
                                                             message.text))

@bot.message_handler(commands=['help'])
def handle_text(message):
    bot.send_message(message.from_user.id, "Введи город, получи результат")

@bot.message_handler(commands=['start'])
def handle_text(message):

    user_markup.row('Добавить город в избранное')
    bot.send_message(message.from_user.id, "Введи город, получи результат", reply_markup=user_markup)

@bot.message_handler(commands=['settings'])
def handle_text(message):
    bot.send_message(message.from_user.id, "Введи город, получи результат")

@bot.message_handler(content_types=['text'])

def handle_text(message):
    """
    if message.text == "Добавить в избранное":
        city_add=1
        bot.send_message(message.from_user.id, "Введите город, который нужно добавить:")
        user_markup.row(message.text)
        bot.send_message(message.from_user.id, "added",  reply_markup=user_markup)

    else:
    """
    try:
                city = message.text
                owm = pyowm.OWM('91c713db144e1ce5a94dffd4229169ed')
                observation = owm.weather_at_place(city)
                w = observation.get_weather()
                temperatura = w.get_temperature('celsius')['temp']
                veter = w.get_wind()['speed']
                vlash = w.get_humidity()
                detalstat = w.get_detailed_status()
                log(message)
                bot.send_message(message.from_user.id, "В городе " + city + ":" + "\n"
                + "Температура: " + str(temperatura) + " " + "по Цельсию" + "\n"
                + "Cкорость ветра: " + " " + str (veter)+" м/с" + "\n"\
                +"Влажность: " + str(vlash)+ "%" + "\n")
    except:
                bot.send_message(message.from_user.id, "Нет такого города")
                log(message)
bot.polling(none_stop=True, interval=0)

