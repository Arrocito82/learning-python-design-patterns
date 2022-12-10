from classes.Port.Port import Port

class HTTPSecurePort(Port):
    """A concrete product which represents https port."""
    def __str__(self):
        return '443'