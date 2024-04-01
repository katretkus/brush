import json
import telebot

token = ""
bot = telebot.TeleBot(token)

chat_id = 1606415745
num = 0
questions = {1:
                     ['Твои любимые цвета',
                          {"пастельные тона": 3, "яркие": 2, "темные": 1}
                      ],
                 2:
                     ['ты предпочтешь:',
                          {"пойти в ресторан": 3, "пойти на вечеринку": 2, "пойти в кино": 1}
                      ]
                 }

def save_progress(user_id, question_number):
    progress = {str(user_id): question_number}
    with open('progress.json', 'w') as file:
        json.dump(progress, file)

def load_progress(user_id):
    try:
        with open('progress.json', 'r') as file:
            progress = json.load(file)
            return progress.get(str(user_id))
    except FileNotFoundError:
        return None

@bot.message_handler(commands=['start'])
def handle_start(message):
    save_progress(message.chat.id, 1)  # сбросить прогресс пользователя
    bot.send_message(message.chat.id, "Приветик👋 Интересно а какой ты запах.. Давай узнаем")
    show_question(message.chat.id, 1)

@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.chat.id, "Доступные команды:\n/start - запуск анкеты\n/help - помощь")

def show_question(chat_id, question_number):
    global questions
    question_text = questions[question_number][0]
    options = questions[question_number][1]

    keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
    for option in options:
        keyboard.add(telebot.types.KeyboardButton(option))

    bot.send_message(chat_id, question_text, reply_markup=keyboard)

@bot.message_handler(func=lambda message: True)
def handle_answer(message):
    global num
    user_id = message.chat.id
    progress = load_progress(user_id)
    try:
        if progress is not None:
            if progress < 2:
                num += questions[progress][1][message.text]
                save_progress(user_id, progress + 1)
                show_question(user_id, progress + 1)
            else:
                print(num)
                if num >=5:
                    bot.send_message(message.chat.id, 'Ты пахнешь так же сладко как и сахарная вата🍭')
                    bot.send_message(message.chat.id, 'Нажми /start и начни заново')
                elif num <=4 and num >=2  :
                    bot.send_message(message.chat.id, 'Твой фруктовый запах поднимает настроение🍊')
                    bot.send_message(message.chat.id, 'Нажми /start и начни заново')
                else:
                    bot.send_message(message.chat.id, 'Пряной запах, а по другому элексир уверенности🍪')
                    bot.send_message(message.chat.id, 'Нажми /start и начни заново')
                save_progress(user_id, 1) # сбросить прогресс пользователя
        else:
            bot.send_message(user_id, "Чтобы начать нажмите /start.")
    except Exception as e:
        bot.send_message(message.chat.id, 'Что - то не так🤔 нажми /start')
bot.polling()
