class Borg(object):
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Borg, cls).__new__(cls, *args, **kwargs)
        """"
        __dict__ almacena el estado de la instancia.
        En este caso a todas las nuevas instancias se le asignan _shared_state,
        es decir todos los estados de nuevas instancias apuntan a la variable
        _shared_stare de la clase Borg.
        """
        obj.__dict__ = cls._shared_state
        return obj
        
class Child(Borg):
    pass

class AnotherChild(Borg):
    _shared_state={}
