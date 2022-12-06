from Borg import Borg, Child, AnotherChild
borg = Borg()
another_borg = Borg()
print(borg is another_borg) # son diferentes instancias
child = Child()
borg.only_one_var = "I'm the only one var" # se agrego la variable only_one_var al estado _shared_state
print(child.only_one_var) # comprobando que comparten el estado


# funciona aún con nuevas instancias
child2=Child()
print(child2.only_one_var) 

# modificando el estado
child.only_one_var="I've Changed" 
# Comprobando el estado compartido
print(child2.only_one_var)
print(child.only_one_var) 
print(borg.only_one_var) 
print(another_borg.only_one_var) 

# ahora si no quisieramos un estado compartido
child3=AnotherChild()
# ya no se comparte el estado
print(child3.only_one_var) 

'''
Traceback (most recent call last):
  File "/home/andrea/learning-python-design-patterns/borg-singleton/main.py", line 24, in <module>
    print(child3.only_one_var) 
AttributeError: 'AnotherChild' object has no attribute 'only_one_var'
'''
