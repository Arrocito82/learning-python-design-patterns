import time
from classes.EUTimeObserver import EUTimeObserver
from classes.USATimeObserver import USATimeObserver
from classes.Subject import Subject


if __name__ == '__main__':
    subject = Subject()
    print 'Adding usa_time_observer'
    observer1 = USATimeObserver('usa_time_observer')
    subject.register_observer(observer1)
    subject.notify_observers()
    time.sleep(2)
    print 'Adding eu_time_observer'
    observer2 = EUTimeObserver('eu_time_observer')
    subject.register_observer(observer2)
    subject.notify_observers()
    time.sleep(2)
    print 'Removing usa_time_observer'
    subject.unregister_observer(observer1)
    subject.notify_observers()
