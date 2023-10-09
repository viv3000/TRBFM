import telebot;
from   telebot import types;

import time

from handlers.commands import commands_handler;
from handlers.message import message_handler;
from handlers.callback_query import callback_handler;

import helper;

bot = telebot.TeleBot(helper.helper.getToken()[0][:-1]);

commands_handler(bot);
message_handler(bot);
callback_handler(bot);


bot.polling(none_stop=True, interval=5)
"""
try:
    bot.polling(none_stop=True, interval=10)
except Exception as err:
    time.sleep(5)
    print("Internet error!")
#bot.polling(none_stop=True, interval=0)
"""
