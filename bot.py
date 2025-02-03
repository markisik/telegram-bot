import telebot
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("token")
API = os.getenv("API")

bot = telebot.TeleBot(token)

def extract_arg(arg):
    return arg.split()[1:]

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, рад тебя видеть!')

@bot.message_handler(commands=['porno'])
def porno(message):
   bot.send_message(message.chat.id, 'А ВОТ НЕТУ ТУТ ПОРНУХИ')

@bot.message_handler(commands=['love'])
def love(message):
   bot.send_message(message.chat.id, 'Дарую тебе мою любовь')
   for i in range(50):
    bot.send_message(message.chat.id, '❤️')
   bot.send_message(message.chat.id, 'Секретая команда для моей любимой светы❤️')


@bot.message_handler(commands=['w'])
#@bot.message_handler(content_types=['text'])
def weather(message):
    #bot.send_message(message.chat.id, 'Введите город')
    city = extract_arg(message.text.strip().lower())
    #city = message.text.strip().lower()
    bot.send_message(message.chat.id, 'Проверка...')
    city1 = ''.join(city)
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city1}&appid={API}&units=metric')
    print(city1)
    if res.status_code != 200:
        bot.reply_to(message, f'Город указан не верно, не забудьте написать команду с городом')
        return
    data = json.loads(res.text)
    temp = data["main"]["temp"]
    wind = data["wind"]["speed"]
    wind_degree = data["wind"]["deg"]
    tempmin = data["main"]["temp_min"]
    tempmax = data["main"]["temp_max"]
    bot.reply_to(message, f'Cейчас температура: {temp}' + "\n" + f'Минимальная температура: {tempmin}' + "\n" + f'Максимальная температура: {tempmax}' + "\n" + f'Скорость ветра: {wind}м\с' + "\n" + f'Направление ветра: {wind_degree}')
    #image = 'sun.png' if temp > 5.0 else 'sunny.png'
    #file = open('./picters/' + image, 'rb')
    #bot.send_photo(message.chat.id, file)    

bot.polling(non_stop=True)
