# GameOfLife
El juego empieza apenas inicias al pregroma, recuerda que lo puede pausar en cualquier momento precionana cualquier tecla del teclado.
Cuando el juego este pausado podras **seleccionar** las diferentes casillas en las que quieres que este se incialice con el click **izquierdo**.
Puedes **borrar** las casillas con el click **derecho**

Sideseas ejecutar desde VS code necesitaras configurar el settings.json.
Para ello presiona CTR + SHIFT + P
Choose "Preferences: Open Settings (JSON)"
Acontinuacion agrega al JSON la el siguiente elemento.

```
"python.linting.pylintArgs": ["--generate-members"]
```

Si esto no te funciono, puede intentar agregando las siguientes lineas

``` 
"python.linting.pylintArgs":[
    "--extension-pkg-whitelist=pygame",
    "--erros-only"
]
```