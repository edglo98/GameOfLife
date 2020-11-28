# GameOfLife
El Juego de la vida es un autómata celular diseñado por el matemático británico John Horton Conway en 1970.

El juego sigue un patrón que esta determinado por su estado inicial el cual va evolucionando a través del tiempo siguiendo dos sencillas reglas

- Una célula muerta con exactamente 3 células vecinas vivas "nace" (es decir, al turno siguiente estará viva).
- Una célula viva con 2 o 3 células vecinas vivas sigue viva, en otro caso muere (por "soledad" o "superpoblación").
 
Para correr el juego deberás tener instalado [python](https://www.python.org/)
El juego empieza apenas inicias al programa, recuerda que lo puede pausar en cualquier momento precionana cualquier tecla del teclado.

```
    pip install pygame
    pip install numpy
```

El juego empieza apenas inicias al programa, recuerda que lo puede pausar en cualquier momento presionando cualquier tecla del teclado.
cuando el juego este pausado las casillas serán grises y cuando este iniciado se colorearan de blanco.
Cuando el juego este pausado podrás **seleccionar** las diferentes casillas con el clic **izquierdo**, en las cuales se iniciara .
Puedes **borrar** las casillas con el clic **derecho**

Si deseas ejecutar desde VS code necesitaras configurar el settings.json.
Para ello presiona **CTR + SHIFT + P**
Busca "Preferences: Open Settings (JSON)"
Continuación agrega al JSON la el siguiente elemento.

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
