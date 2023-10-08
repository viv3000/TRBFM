import telebot;
from   telebot import types;

from datetime import datetime, timedelta;

from log import Log

def callback_handler(bot):
    @bot.callback_query_handler(func=lambda call: True)
    def callback_worker(call):
        Log().log(f'server: {call.from_user.username}: call.data:{call.data}')
        bot.send_document(call.from_user.id, call.data);
