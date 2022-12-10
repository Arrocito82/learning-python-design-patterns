from classes.Port.Port import Port

class FTPPort(Port):
    """A concrete product which represents ftp port."""
    def __str__(self):
        return '21'