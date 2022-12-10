from classes.Proxy import Proxy


if __name__ == '__main__':
    proxy1 = Proxy()
    print
    proxy2 = Proxy()
    print
    proxy3 = Proxy()
    print
    proxy1.sort(reverse=True)
    print
    print 'Deleting proxy2'
    del proxy2
    del proxy1
    del proxy3
    print
    proxy4 = Proxy()
    print
    proxy4.sort(reverse=True)
    print

    print 'The other objects are deleted upon program termination'
