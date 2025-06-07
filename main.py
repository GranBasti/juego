import pygame

import constantes
from personaje import Personaje


pygame.init()

#Variables de ventana
#ancho = 800
#alto = 600

ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))

#Cambiar el nombre de la ventana
pygame.display.set_caption("Mi primer juego")

jugador = Personaje(100,100)


#Definir las variable de movimiento del jugador
mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False

# Controlar los frama rate
reloj = pygame.time.Clock()


#Variable
run = True

#LOOP para mantener la ventana abierta
while run:

    #60 FPS Frame Rate
    reloj.tick(constantes.FPS)

    ventana.fill(constantes.COLOR_BG)

    #Calcular el movimiento del jugador
    delta_x = 0
    delta_y = 0

    if mover_derecha == True:
        delta_x = constantes.VELOCIDAD
    if mover_izquierda == True:
        delta_x = -constantes.VELOCIDAD
    if mover_arriba == True:
        delta_y = -constantes.VELOCIDAD
    if mover_abajo == True:
        delta_y = constantes.VELOCIDAD


    #Mover el jugador
    jugador.movimiento(delta_x, delta_y)


    jugador.dibujar(ventana)


    for event in pygame.event.get():
        #Para cerrar el juego
        if event.type == pygame.QUIT:
            run = False

        #Mover jugador
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                mover_izquierda = True
            if event.key == pygame.K_w:
                mover_arriba = True
            if event.key == pygame.K_s:
                mover_abajo = True
            if event.key == pygame.K_d:
                mover_derecha = True


        #para cuando se suelta la tecla
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                mover_izquierda = False
            if event.key == pygame.K_w:
                mover_arriba = False
            if event.key == pygame.K_s:
                mover_abajo = False
            if event.key == pygame.K_d:
                mover_derecha = False



    #Para actualizar la ventana
    pygame.display.update()

pygame.quit()