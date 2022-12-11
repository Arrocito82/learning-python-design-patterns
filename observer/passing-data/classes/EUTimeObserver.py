import datetime
from classes.Observer import Observer


class EUTimeObserver(Observer):
    def __init__(self, name):
        self.name = name

    def notify(self, unix_timestamp):
        time = datetime.datetime.fromtimestamp(
            int(unix_timestamp)).strftime('%Y-%m-%d %H:%M:%S')
        print 'Observer', self.name, 'says:', time
