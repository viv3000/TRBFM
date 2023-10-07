import telebot;
from   telebot import types;

def message_handler(bot):
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
    
