from classes.Port.Port import Port

class HTTPPort(Port):
    """A concrete product which represents http port."""
    def __str__(self):
        return '80'