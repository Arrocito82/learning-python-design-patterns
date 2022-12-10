from Singletone import Singleton, Child

child = Child()
singleton = Singleton()
another_singleton = Singleton()
print(singleton is another_singleton)

singleton.only_one_var = "I'm only one var"
print(another_singleton.only_one_var)

'''
si creo child después de inicializar la clase padre Singleton (linea 19), 
no hay problema porque la clase Singleton ya había sido inicializada antes (linea 4),
pero si lo inicializo antes que Singletone (linea 3), que es la clase padre, entonces me da el error
AttributeError: 'Child' object has no attribute 'only_one_var'
porque a ese punto cuando fue asignada aún no existia la variable only_one_var
''' 

# child = Child()
print(child is singleton)
print(child.only_one_var)