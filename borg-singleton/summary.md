# Borg Singleton
## Summary
- En este singleton, todas las instancias son nuevas y diferentes,
la diferencia con el classic singleton y el module-level singleton
es que lo único que comparten todas las instancias es el estado.
- En este ejemplo es el _shared_state, el cual es una variable de la clase
y por ende se mantiene única dado que la clase solo se instancia una vez.
- Por otro lado todas las nuevas instancias **apuntan** a la misma instancia de 
_shared_state, por ende cualquier cambio que se haga en el estado de una instancia
afectara a todas las instancias de born singleton e inclusive sus hijos.

## Execute
```
python3 main.py
```


