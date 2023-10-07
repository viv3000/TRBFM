import telebot;
from   telebot import types;

from datetime import datetime, timedelta;

def callback_handler(bot):
    @bot.callback_query_handler(func=lambda call: True)
    def callback_worker(call):
        print(call.data)
        date = datetime.strptime(call.data, "%Y-%m-%d");
        url = f'https://mkeiit.ru/wp-content/uploads/{date.year}/{date.month}/{date.day}.{date.month}.{date.year}.pdf';
        bot.send_document(call.from_user.id, url);
