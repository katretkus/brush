
import telebot


token = ""
bot = telebot.TeleBot(token)

chat_id = 1606415745
num = 0

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Я могу рассказать тебе о Японии. напиши команду /info")

@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id, "Япония страна разбитая на 4 главных острова, а столица Японии - Токио расположен на острове Хонсю.")
    bot.send_message(message.chat.id, "Ты можешь узнать интересный факт. Но для начала выбери цифру от 1 до 3")

@bot.message_handler(commands=['fact'])
def fact(message):
    if num == 1:
        bot.send_message(message.chat.id, "Знал ли ты что по-японски Япония будет - Нихон.")
    elif num == 2:
        bot.send_message(message.chat.id, "Самая высокая гора в Японии это - Фудзияма.")
    elif num == 3:
        bot.send_message(message.chat.id, "В Японии есть сезон дождей который длится c начала июня до середины июля!")
    else:
        bot.send_message(message.chat.id, "упс, ошибка видимо не та циферка")

@bot.message_handler()
def save_num(message):
    # Проверяем, что возраст - число
    if not message.text.isdigit():
        bot.send_message(message.chat.id, "Пока что я не знаю как реагировать на такое😳")
    else:
        # Запоминаем присланный возраст в глобальную переменную `age`, объявленную в начале программы
        global num
        num = int(message.text)
        bot.send_message(message.chat.id, "Отлично, я запомнила) Теперь можешь использовать команду /fact")

bot.polling()
