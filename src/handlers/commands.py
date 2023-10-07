import telebot;
from   telebot import types;

from datetime import datetime, timedelta;

import requests;

from templates.btn import btn;

def commands_handler(bot):
    @bot.message_handler(commands = ['getTimetable'])
    def getTimetableHandler(message):
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
    
    
    @bot.message_handler(commands = ['start'])
    def startHandler(message):
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
