import datetime
from classes.Observer import Observer
from classes.Subject import Subject

class EUTimeObserver(Observer):
    def __init__(self, name):
        self.name = name

    def notify(self, subject):
        time = datetime.datetime.fromtimestamp(
            int(subject.cur_time)).strftime('%Y-%m-%d %H:%M:%S')
        print 'Observer', self.name, 'says:', time
