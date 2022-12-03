from Borg import Borg, Child
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
