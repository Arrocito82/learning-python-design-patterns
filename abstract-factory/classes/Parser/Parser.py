import abc

class Parser(object):
    """An abstract product, represents parser to parse web content.
    One of its subclasses will be created in factory methods."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __call__(self, content):
        pass
