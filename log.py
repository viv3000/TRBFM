from datetime import datetime

class Log:
    def log(self, message, user=None, error=None):
        if (user is None):
            log = f'message {message}; error: {error}\n'
        else:
            if (user.username is not None):
                log = f'user: {user.username}; message {message}; error: {error}\n'
            elif (user.first_name is not None):
                log = f'user: {user.first_name}; message {message}; error: {error}\n'
            else:
                log = f'user: {user.id}; message {message}; error: {error}\n'

        f = open("log.txt", "a")
        f.write(str(datetime.now()) + "; " + log)
        f.close()
        print(log)
