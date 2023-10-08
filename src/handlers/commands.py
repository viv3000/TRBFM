import telebot;
from   telebot import types;
from datetime import datetime, timedelta, date;

from templates.btn import btn;
from templates.Timetables import Timetables;
from templates.Timetables import Timetable;

from log import Log;

class TimetableBtn():
    def __init__(self, timetable: Timetable):
        self.timetable = timetable
        self.weekdays = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]

    def to_button(self) -> telebot.types.InlineKeyboardButton:
        message = f'{self.weekdays[self.timetable.weekday]}\n({self.timetable.date})'
        return types.InlineKeyboardButton(text=message, callback_data=self.timetable.href)

def commands_handler(bot):
    @bot.message_handler(commands = ['getTimetable'])
    def getTimetableHandler(message):
        Log().log(message.from_user.username + ': \getTimetable');
        markup = types.InlineKeyboardMarkup();
    
        btns = []
        today = date.today()
        week = today.isocalendar()[1]
        timetables = Timetables().get_timetables_url()
        for i in timetables[today.year][today.month]:
            timetable = timetables[today.year][today.month][i]
            if(timetable.week == week) or (timetable.week == week+1):
                btns.append(TimetableBtn(timetable))

        for i in btns: markup.add(i.to_button())

        bot.send_message(message.from_user.id, "Тебе необходимо выбрать дату, ты справишься?", reply_markup = markup);
    
    @bot.message_handler(commands = ['start'])
    def startHandler(message):
        Log().log(message.from_user.username + ': \start');
        markup = types.ReplyKeyboardMarkup();
    
        btns = {
            btn("в сайт калледжа хочу ссылочку") : "",
            btn("в гитхаб хочу ссылочку") : "",
            btn("в порнхаб хочу ссылочку") : "",
            btn("списочек коммандочек") : "",
        }
        for i in btns: 
            markup.add(types.InlineKeyboardButton(text=i.text))
    
        bot.send_message(message.from_user.id, "Приветульки малышь!!!\n /getTimetable - попросить расписание\n /start - начать общение сначала", reply_markup = markup);
