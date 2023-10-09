import telebot;
from   telebot import types;

from datetime import datetime, timedelta;
from templates.ConverterPdfToJpg import ConverterPdfToJpg

from log import Log

def callback_handler(bot):
    @bot.callback_query_handler(func=lambda call: True)
    def callback_worker(call):
        Log().log(f'server: call.data:{call.data}', call.from_user)

        jpgs = ConverterPdfToJpg().convert(call.data);
        for i in jpgs:
            bot.send_photo(call.from_user.id, photo=open(i, 'rb'));
