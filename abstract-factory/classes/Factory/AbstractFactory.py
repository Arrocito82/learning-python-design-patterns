import abc

class AbstractFactory(object):
    """Abstract factory interface provides 3 methods to implement in its
    subclasses: create_protocol, create_port and create_parser."""
    __metaclass__ = abc.ABCMeta

    def __init__(self, is_secure):
        """if is_secure is True, factory tries to make connection secure,
        otherwise not"""
        self.is_secure = is_secure

    @abc.abstractmethod
    def create_protocol(self):
        pass

    @abc.abstractmethod
    def create_port(self):
        pass

    @abc.abstractmethod
    def create_parser(self):
        pass
