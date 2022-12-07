from classes.Factory.AbstractFactory import AbstractFactory
from classes.Parser.FTPParser import FTPParser
from classes.Port.FTPPort import FTPPort

class FTPFactory(AbstractFactory):
    """Concrete factory for building FTP connection."""
    def create_protocol(self):
        return 'ftp'
    def create_port(self):
        return FTPPort()
    def create_parser(self):
        return FTPParser()