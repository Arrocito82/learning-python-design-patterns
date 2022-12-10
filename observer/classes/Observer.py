from abc import ABCMeta, abstractmethod
import datetime


class Observer(object):
    """Abstract class for observers, provides notify method as
    interface for subjects."""
    __metaclass__ = ABCMeta

    @abstractmethod
    def notify(self, unix_timestamp):
        pass
