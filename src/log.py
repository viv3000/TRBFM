class Log:
    def log(self, message, error=None):
        log = f'{message}:   {error}\n'
        f = open("log.txt", "a")
        f.write(log)
        f.close()
        print(log)
