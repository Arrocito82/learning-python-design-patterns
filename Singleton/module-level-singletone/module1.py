import singletone
print (singletone.only_one_var)
singletone.only_one_var += " after modification"
# imprime la misma variable only_one_var, pero si se ha modificado la variable
import module2