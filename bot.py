import telebot
import requests
import json

token = '7107794543:AAGoqTAZZcT1ZuMdTMk6gw-8J5-7WRSZ7uU'

API = '8a754a26e67c3b0effe5f7e22853f89c'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, рад тебя видеть!')

@bot.message_handler(commands=['porno'])
def porno(message):
   bot.send_message(message.chat.id, 'А ВОТ НЕТУ ТУТ ПОРНУХИ')

@bot.message_handler(commands=['love'])
def porno(message):
   bot.send_message(message.chat.id, 'Секретая команда для моей любимой светы❤️')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
     data = json.loads(res.text)
     temp = data["main"]["temp"]
     bot.reply_to(message, f'Cейчас погода: {temp}')
 
     image = 'sunny.png' if temp > 5.0 else 'sun.png'
     file = open('./' + image, 'rb')
     bot.send_photo(message.chat.id, file)
    else:
       bot.reply_to(message, f'Город указан не верно')

bot.polling(non_stop=True)