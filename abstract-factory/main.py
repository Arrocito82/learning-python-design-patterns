import urllib2
from classes.Factory.FTPFactory import FTPFactory
from classes.Factory.HTTPFactory import HTTPFactory
from classes.Connector.Connector import Connector

if __name__ == '__main__':
    domain = 'ftp.freebsd.org'
    path = '/pub/FreeBSD/'
    protocol = input('Connecting to {}. Which Protocol to use? (0-http,1-ftp): '.format(domain))
    if protocol == 0:
        is_secure = bool(input('Use secure connection? (1-yes, 0-no): '))
        factory = HTTPFactory(is_secure)
    elif protocol == 1:
        is_secure = False
        factory = FTPFactory(is_secure)
    else:
        print 'Sorry, wrong answer'
    
    connector = Connector(factory)
    try:
        content = connector.read(domain, path)
    except urllib2.URLError, e:
        print 'Can not access resource with this method'
    print connector.parse(content)
