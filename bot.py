import telebot
import requests
import json
import re
 
token = '7107794543:AAGoqTAZZcT1ZuMdTMk6gw-8J5-7WRSZ7uU'

API = '8a754a26e67c3b0effe5f7e22853f89c'

bot = telebot.TeleBot(token)

def extract_arg(arg):
    return arg.split()[1:]

@bot.message_handler(commands=['start'])
def start(message):
    print(message.from_user.id)
    print(message.from_user.first_name)
    print(message.from_user.last_name)
    print(message.from_user.username)
    print(message.text)
    bot.send_message(message.chat.id, 'Привет, рад тебя видеть!')
    bot.send_message(message.chat.id, 'Вот что я могу:' + "\n" + '/w - погода')
    

@bot.message_handler(commands=['porno'])
def porno(message):
   print(message.from_user.id)
   print(message.from_user.first_name)
   print(message.from_user.last_name)
   print(message.from_user.username)
   print(message.text)
   bot.send_message(message.chat.id, 'А ВОТ НЕТУ ТУТ ПОРНУХИ')
   

@bot.message_handler(commands=['люблю'])
def love(message):
   print(message.from_user.id)
   print(message.from_user.first_name)
   print(message.from_user.last_name)
   print(message.from_user.username)
   print(message.text)
   bot.send_message(message.chat.id, 'Дарую тебе мою любовь')
   for i in range(10):
    bot.send_message(message.chat.id, '❤️')

   bot.send_message(message.chat.id, 'Секретая команда для моей любимой Ани❤️')

@bot.message_handler(commands=['w'])
def weather(message):
    print(message.from_user.id)
    print(message.from_user.first_name)
    print(message.from_user.last_name)
    print(message.from_user.username)
    print(message.text)
    city = message.text
    city = city.replace("/", "", 1)
    city = city.replace("w", "", 1)
    city = city.replace(" ", "", 1)
    print(city)
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
     data = json.loads(res.text)
     temp = data["main"]["temp"]
     wind = data["wind"]["speed"]
     windstorona = data["wind"]["deg"]
     tempmin = data["main"]["temp_min"]
     tempmax = data["main"]["temp_max"]
     bot.reply_to(message, f'Cейчас температура: {temp}°C' + "\n" + f'Минимальная температура: {tempmin}°C' + "\n" + f'Максимальная температура: {tempmax}°C' + "\n" + f'Скорость ветра: {wind}м\с' + "\n" + f'Направление ветра: {windstorona}°')
     #image = 'sun.png' if temp > 5.0 else 'sunny.png'
     #file = open('./picters/' + image, 'rb')
     #bot.send_photo(message.chat.id, file)
    else:    bot.reply_to(message, f'Город указан не верно, не забудьте написать команду с городом')

@bot.message_handler(commands=['stop'])
def stop(message):
    print(message.from_user.id)
    print(message.from_user.first_name)
    print(message.from_user.last_name)
    print(message.from_user.username)
    print(message.text)
    sys.exit(0)
    

bot.polling(non_stop=True)
