import abc

class Port(object):
    __metaclass__ = abc.ABCMeta
    """An abstract product, represents port to connect. One of its
    subclasses will be created in factory methods."""
    @abc.abstractmethod
    def __str__(self):
        pass