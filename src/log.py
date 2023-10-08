from datetime import datetime

class Log:
    def log(self, message, error=None):
        log = f'{message}:   {error}\n'
        f = open("log.txt", "a")
        f.write(str(datetime.now()) + ":" + log)
        f.close()
        print(log)
