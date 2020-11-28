# GameOfLife
El Juego de la vida es un autómata celular diseñado por el matemático británico John Horton Conway en 1970.

El juego sigue un patron que esta determinado por su estado inicial el cual va evolucionando a través del tiempo siguiendo dos sencillas reglas

- Una célula muerta con exactamente 3 células vecinas vivas "nace" (es decir, al turno siguiente estará viva).
- Una célula viva con 2 o 3 células vecinas vivas sigue viva, en otro caso muere (por "soledad" o "superpoblación").
 
Para correr el juego deberas tener instalado [python](https://www.python.org/)
Adicionalmente necesitaras las siguientes librerias.

```
    pip install pygame
    pip install numpy
```

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
