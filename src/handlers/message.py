import telebot;
from   telebot import types;

from log import Log;

def message_handler(bot):
    @bot.message_handler(content_types = ['text'])
    def getTextMessages(message):
        Log().log(f'{message.from_user.username}: {message.text}');
        messages = {
                "в сайт калледжа хочу ссылочку" : "https://mkeiit.ru",
                "в гитхаб хочу ссылочку"        : "https://github.com/viv3000/TRBFM",
                "в порнхаб хочу ссылочку"       : "https://pornhub.com/viv3000",
                "списочек коммандочек"          : "Приветульки малышь!!!\n /start - начать общение сначала\n /getTimetable - попросить расписание \n /getCallTimetable - получить расписание звонков \n /getCallTimetableMonday - получить расписание звонков на понедельник \n /getCallTimetableFriday - получить расписание звонков на пятницу \n /getCallTimetableSaturday - получить расписание звонков на субботу",
        }
        
        try:
            bot.send_message(message.from_user.id, messages[message.text]);
        except KeyError as ex:
            bot.send_message(message.from_user.id, "За такое можно и ручки поотрывать, тестировщик недобитый!!!!");
            Log().log(f'{message.from_user}:{message.text}', ex);
        except Exception as ex:
            bot.send_message(message.from_user.id, "Мы не знаем что это такое, а если бы знали что это такое, мы не знаем что это такое! (пиши сюда: /dev/null)");
            Log().log(f'{message.from_user}:{message.text}', ex);
    
