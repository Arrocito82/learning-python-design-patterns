import datetime
from classes.Observer import Observer

class USATimeObserver(Observer):
    def __init__(self, name):
        self.name = name

    def notify(self, subject):
        time = datetime.datetime.fromtimestamp(int(subject.cur_time)).strftime('%Y-%m-%d %I:%M:%S%p')
        print 'Observer', self.name, 'says:', time
