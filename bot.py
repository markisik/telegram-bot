import telebot
import requests
import json
import datetime
 
token = '7107794543:AAGoqTAZZcT1ZuMdTMk6gw-8J5-7WRSZ7uU'

API = ''

bot = telebot.TeleBot(token)

def extract_arg(arg):
    return arg.split()[1:]

@bot.message_handler(commands=['start'])
def start(message):
    now = datetime.datetime.now()
    print(f'ID user: {message.from_user.id} \nName user: {message.from_user.first_name} {message.from_user.last_name} \nNickname user: {message.from_user.username} \nCommand user: {message.text} \n{now} \n------------')
    bot.send_message(message.chat.id, 'Привет, рад тебя видеть!')
    bot.send_message(message.chat.id, 'Вот что я могу:' + "\n" + '/w - погода')
    

@bot.message_handler(commands=['porno'])
def porno(message):
   now = datetime.datetime.now()
   print(f'ID user: {message.from_user.id} \nName user: {message.from_user.first_name} {message.from_user.last_name} \nNickname user: {message.from_user.username} \nCommand user: {message.text} \n{now} \n------------')
   bot.send_message(message.chat.id, 'А ВОТ НЕТУ ТУТ ПОРНУХИ')
   

@bot.message_handler(commands=['люблю'])
def love(message):
   now = datetime.datetime.now()
   print(f'ID user: {message.from_user.id} \nName user: {message.from_user.first_name} {message.from_user.last_name} \nNickname user: {message.from_user.username} \nCommand user: {message.text} \n{now} \n------------')

   bot.send_message(message.chat.id, 'пусто')

@bot.message_handler(commands=['w'])
def weather(message):
    now = datetime.datetime.now()
    print(f'ID user: {message.from_user.id} \nName user: {message.from_user.first_name} {message.from_user.last_name} \nNickname user: {message.from_user.username} \nCommand user: {message.text} \n{now} \n------------')
    city = message.text
    city = city.replace("/", "", 1)
    city = city.replace("w", "", 1)
    city = city.replace(" ", "", 1)
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
    else:    bot.reply_to(message, f'Город указан не верно, не забудьте написать команду с городом!')

@bot.message_handler(commands=['stop'])
def stop(message):
    now = datetime.datetime.now()
    print(f'ID user: {message.from_user.id} \nName user: {message.from_user.first_name} {message.from_user.last_name} \nNickname user: {message.from_user.username} \nCommand user: {message.text} \n{now} \n------------')
    SystemExit.exit(0)

@bot.message_handler(content_types=['text'])
def text(message):
    now = datetime.datetime.now()
    print(f'ID user: {message.from_user.id} \nName user: {message.from_user.first_name} {message.from_user.last_name} \nNickname user: {message.from_user.username} \nCommand user: {message.text} \n{now} \n------------')
    bot.send_message(message.chat.id, 'Если честно, я не понял что ты сказал')
    
if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True, interval=0)
        except Exception as e:
            now = datetime.datetime.now()
            print(f'!---Ошибка в {now}, продолжение работы---!')
