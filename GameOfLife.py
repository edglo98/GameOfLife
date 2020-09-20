import pygame
import numpy as np
import time, os

# Hago que la ventana aparezca centrada en Windows
os.environ["SDL_VIDEO_CENTERED"] = "1"

#iniciamos pygame
pygame.init()

#Titulo de la ventana
pygame.display.set_caption("Juego de la vida")

#creamos una patalla definiendo los pixeles.
width, height = 800, 800
screen = pygame.display.set_mode((height, width))

#Pintamos el color de fondo de la pantalla
bg = 25,25,25
screen.fill(bg)

#definimos el numero de celdas que queremos que tenga el juego
nxC, nyC = 35, 35

dimCW = width / nxC
dimCH = height / nyC

#Estado de las celdas. vivas = 1, muertas = 0.
gameState = np.zeros((nxC, nyC))

#control de pausa
pauseExect = False

# Cantidad de iteraciones:
iteration = 0

#Bucle de ejecucion
#para que la pantalla se muestre indefinidamentes tenemos que crear un bucle
while True:

    #mantener la copia del estado en ejecucion del juego para relacionarlo con el estado posterior en cada ejecucion del ciclo
    newGameState = np.copy(gameState)

    #por cada iteracion limpiamos la pantalla
    screen.fill(bg)
    time.sleep(.2)

    #Registramos eventos de teclado y raton
    ev = pygame.event.get()

    # Contador de población:
    population = 0
    
    for event in ev:
        #se detecta si se presiona una tecla
        if event.type == pygame.KEYDOWN:
            pauseExect = not pauseExect
        #Escuchamos el boton de mouse
        mouseClick = pygame.mouse.get_pressed()
        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
            newGameState[celX, celY] = not mouseClick[2]

    for y in range(0, nxC):
        for x in range(0, nyC):
            if not pauseExect:
                #Calculamos el número de vecinos cercanos
                n_neigh = (
                    gameState[(x - 1) % nxC, (y - 1) % nyC]
                    + gameState[x % nxC, (y - 1) % nyC]
                    + gameState[(x + 1) % nxC, (y - 1) % nyC]
                    + gameState[(x - 1) % nxC, y % nyC]
                    + gameState[(x + 1) % nxC, y % nyC]
                    + gameState[(x - 1) % nxC, (y + 1) % nyC]
                    + gameState[x % nxC, (y + 1) % nyC]
                    + gameState[(x + 1) % nxC, (y + 1) % nyC]
                )

                #Regla #1: una celda muerta con exactamente 3 vecinas vivas, "revive"
                if gameState[x, y] == 0 and n_neigh == 3:
                    newGameState[x, y] = 1
                
                #Regla #2: una celda viva con menos de 2 o más de 3 vecinos vivas, "muere"
                elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    newGameState[x, y] = 0

            #Creamos el poligono de cada celda a dibujar
            poly = [
                (int((x) * dimCW), int(y * dimCH)),
                (int((x+1) * dimCW), int(y * dimCH)),
                (int((x+1) * dimCW), int((y + 1) * dimCH)),
                (int((x) * dimCW), int((y + 1) * dimCH))
            ]
            #dibujamos la celda para cada par de x e y con un ancho de 1px
            if newGameState[x, y] == 0:
                pygame.draw.polygon(screen, (128,128,128), poly, 1)
            else:
                if pauseExect:
                    # Con el juego pausado pinto de gris las celdas
                    pygame.draw.polygon(screen, (128, 128, 128), poly, 0)
                else:
                    # Con el juego ejecutándose pinto de blanco las celdas
                    pygame.draw.polygon(screen, (255, 255, 255), poly, 0)
    #Actualizamos el estado del juego
    gameState = np.copy(newGameState)
    #Actualiza la pantalla.
    pygame.display.flip()
