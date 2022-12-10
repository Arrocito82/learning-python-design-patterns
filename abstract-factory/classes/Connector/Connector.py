import abc
import urllib2

class Connector(object):
    """A client."""

    def __init__(self, factory):
        """factory is a AbstractFactory instance which creates all
        attributes of a connector according to factory class."""
        self.protocol = factory.create_protocol()
        self.port = factory.create_port()
        self.parse = factory.create_parser()

    def read(self, host, path):
        url = self.protocol + '://' + host + ':' + str(self.port) + path
        print 'Connecting to ', url
        return urllib2.urlopen(url, timeout=2).read()

    @abc.abstractmethod
    def parse(self):
        pass
