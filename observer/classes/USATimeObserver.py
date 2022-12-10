import datetime
from classes.Observer import Observer

class USATimeObserver(Observer):
    def __init__(self, name):
        self.name = name

    def notify(self, unix_timestamp):
        time = datetime.datetime.fromtimestamp(int(unix_timestamp)).strftime('%Y-%m-%d %I:%M:%S%p')
        print 'Observer', self.name, 'says:', time
