from urllib.request import urlopen
from bs4 import BeautifulSoup

import datetime

class Timetable:
    def __init__(self, weekday, week, date, href):
        self.weekday = weekday
        self.week    = week
        self.date    = date
        self.href    = href

class Timetables:
    def __init__(self, url:str="https://mkeiit.ru/?page_id=2699"):
        self.soup = BeautifulSoup(urlopen(url), 'html.parser')

    def get_timetables_url(self) -> dict[int, dict[int, dict[int, Timetable]]]:
        d = {}
        for i in self.soup.findAll('td'): 
            if (i is not None) and (i.strong is not None) and (i.strong.a is not None):
                href = i.strong.a['href']
                date = href[href.rfind('/')+1:-4]

                beginPoint = date.find('.')
                lastPoint = date.rfind('.')
                    
                month = int(date[beginPoint+1:lastPoint])
                day   = int(date[:beginPoint])
                year  = int(date[-4:])

                week    = datetime.datetime(year, month, day).isocalendar()[1]
                weekday = datetime.datetime(year, month, day).weekday()

                if( year not in d):
                    d[year] = {}
                if(month not in d[year]):
                    d[year][month] = {}

                d[year][month][day] = Timetable(weekday, week, date, href)

        return d;
