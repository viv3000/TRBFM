import telebot;
from   telebot import types;

from datetime import datetime, timedelta;

import requests;

import helper;

bot = telebot.TeleBot(helper.helper.getToken()[0][:-1]);

class btn:
    def __init__(self, text, callback_data=None):
        self.text = text
        self.callback_data = callback_data

@bot.message_handler(commands = ['start'])
def url(message):
    print(message.from_user)
    markup = types.ReplyKeyboardMarkup();

    btns = {
            btn("в сайт калледжа хочу ссылочку") : "",
            btn("в гитхаб хочу ссылочку") : "",
            btn("в порнхаб хочу ссылочку") : "",
            btn("/getTimetable") : "/getTimetable",
            btn("/start") : "/start",
    }
    for i in btns: 
        markup.add(types.InlineKeyboardButton(text=i.text))

    bot.send_message(message.from_user.id, "Приветульки малышь!!!\n /getTimetable - попросить расписание\n /start - начать общение сначала", reply_markup = markup);


@bot.message_handler(commands = ['getTimetable'])
def url(message):
    markup = types.InlineKeyboardMarkup();

    btns = []
    for i in range (10): 
        day = (datetime.now() - timedelta(days=i-6))
        url = f'https://mkeiit.ru/wp-content/uploads/{day.year}/{day.month}/{day.day}.{day.month}.{day.year}.pdf'
        if requests.get(url).status_code == 200:
            dateFormat = (str(day.year)  + "-" + 
                         str(day.month) + "-" + 
                         str(day.day))

            btns.append(btn(dateFormat))

    for i in btns:
        markup.add(types.InlineKeyboardButton(text="Расписание на " + i.text, callback_data=i.text))

    bot.send_message(message.from_user.id, "Тебе необходимо выбрать дату, ты справишься?", reply_markup = markup);

@bot.message_handler(content_types = ['text'])
def getTextMessages(message):
    messages = {
            "в сайт калледжа хочу ссылочку" : "https://mkeiit.ru",
            "в гитхаб хочу ссылочку"        : "https://github.com/viv3000/TRBFM",
            "в порнхаб хочу ссылочку"       : "https://pornhub.com/viv3000",

            "/getTimetable" : "/getTimetable",
            "/start"        : "/start"
    }
    
    try:
        if message.text[0] != '/':
            bot.send_message(message.from_user.id, messages[message.text]);
    except KeyError:
        bot.send_message(message.from_user.id, "За такое можно и ручки поотрывать, тестировщик недобитый!!!!");
    except Exception:
        bot.send_message(message.from_user.id, "Мы не знаем что это такое, а если бы знали что это такое, мы не знаем что это такое! (пиши сюда: /dev/null)");

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    print(call.data)
    date = datetime.strptime(call.data, "%Y-%m-%d");
    url = f'https://mkeiit.ru/wp-content/uploads/{date.year}/{date.month}/{date.day}.{date.month}.{date.year}.pdf';
    bot.send_document(call.from_user.id, url);

bot.polling(none_stop=True, interval=0)
