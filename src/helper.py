class helper:
    def getToken():
        with open('token.txt') as f:
            lines = f.readlines();
        return lines;

