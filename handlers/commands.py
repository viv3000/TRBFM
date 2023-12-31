import telebot;
from   telebot import types;
from datetime import datetime, timedelta, date;

from templates.btn import btn;
from templates.Timetables import Timetables;
from templates.Timetables import Timetable;
from templates.TimetableBtn import TimetableBtn
from templates.ConverterPdfToJpg import ConverterPdfToJpg

from log import Log;
   
def commands_handler(bot):
    @bot.message_handler(commands = ['start'])
    def startHandler(message):
        Log().log(': \start', message.from_user);
        markup = types.ReplyKeyboardMarkup();
    
        btns = {
            btn("Контакты") : "",
            btn("Списочек коммандочек") : "",
        }
        for i in btns: 
            markup.add(types.InlineKeyboardButton(text=i.text))
    
        bot.send_message(message.from_user.id, "Приветульки малышь!!!\n /start - начать общение сначала\n /getTimetable - попросить расписание \n /getCallTimetable - получить расписание звонков \n /getCallTimetableMonday - получить расписание звонков на понедельник \n /getCallTimetableFriday - получить расписание звонков на пятницу \n /getCallTimetableSaturday - получить расписание звонков на субботу", reply_markup = markup);

    @bot.message_handler(commands = ['getTimetable'])
    def getTimetableHandler(message):
        Log().log(': \getTimetable', message.from_user);
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

    @bot.message_handler(commands = ['getCallTimetable'])
    def getCallTimetableHandler(message):
        Log().log(': \getCallTimetable', message.from_user);
        jpgs = ConverterPdfToJpg().convert(
            "https://mkeiit.ru/wp-content/uploads/2023/09/Расписание-звонков-основное-.pdf")
        for i in jpgs:
            bot.send_photo(message.from_user.id, photo=open(i, 'rb'));
    
    @bot.message_handler(commands = ['getCallTimetableMonday'])
    def getCallTimetableMondayHandler(message):
        Log().log(': \getCallTimetableMonday', message.from_user);
        jpgs = ConverterPdfToJpg().convert(
            "https://mkeiit.ru/wp-content/uploads/2023/09/Расписание-звонков-на-понедельник-.pdf")
        for i in jpgs:
            bot.send_photo(message.from_user.id, photo=open(i, 'rb'));
    
    @bot.message_handler(commands = ['getCallTimetableFriday'])
    def getCallTimetableFridayHandler(message):
        Log().log(': \getCallTimetableFriday', message.from_user);
        jpgs = ConverterPdfToJpg().convert(
            "https://mkeiit.ru/wp-content/uploads/2023/09/Расписание-звонков-на-пятницу-.pdf")
        for i in jpgs:
            bot.send_photo(message.from_user.id, photo=open(i, 'rb'));
    
    @bot.message_handler(commands = ['getCallTimetableSaturday'])
    def getCallTimetableSaturdayHandler(message):
        Log().log(': \getCallTimetableSaturday', message.from_user);
        jpgs = ConverterPdfToJpg().convert(
            "https://mkeiit.ru/wp-content/uploads/2023/09/Расписание-звонков-суббота.pdf")
        for i in jpgs:
            bot.send_photo(message.from_user.id, photo=open(i, 'rb'));

