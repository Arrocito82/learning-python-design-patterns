from classes.Factory.AbstractFactory import AbstractFactory
from classes.Parser.HTTPParser import HTTPParser
from classes.Port.HTTPPort import HTTPPort
from classes.Port.HTTPSecurePort import HTTPSecurePort

class HTTPFactory(AbstractFactory):
    """Concrete factory for building HTTP connection."""

    def create_protocol(self):
        if self.is_secure:
            return 'https'
        return 'http'

    def create_port(self):
        if self.is_secure:
            return HTTPSecurePort()
        return HTTPPort()

    def create_parser(self):
        return HTTPParser()
