import telebot;
from   telebot import types;

from templates.btn import btn;
from templates.Timetables import Timetables;
from templates.Timetables import Timetable;

class TimetableBtn():
    def __init__(self, timetable: Timetable):
        self.timetable = timetable
        self.weekdays = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]

    def to_button(self) -> telebot.types.InlineKeyboardButton:
        message = f'{self.weekdays[self.timetable.weekday]}\n({self.timetable.date})'
        return types.InlineKeyboardButton(text=message, callback_data=self.timetable.href)
 
