import pygame

import constantes
from personaje import Personaje
from weapon import Weapon

pygame.init()

#Variables de ventana
#ancho = 800
#alto = 600

ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA,
                                   constantes.ALTO_VENTANA))

#Cambiar el nombre de la ventana
pygame.display.set_caption("Mi primer juego")

def escalar_img(image, scale):
    w = image.get_width()
    h = image.get_height()
    nueva_imagen = pygame.transform.scale(image, (w*scale, h*scale))
    return nueva_imagen


#Importar imagenes

#Personaje
animaciones = []
for i in range (8):
    img = pygame.image.load(f"assets//images//characters//player//Run_{i}.png").convert_alpha()
    ima = escalar_img(img, constantes.SCALA_PERSONAJE)
    animaciones.append(img)

#Arma
imagen_shuriken = pygame.image.load(f"assets//images//weapons//01.png").convert_alpha()
imagen_shuriken = escalar_img(imagen_shuriken, constantes.SCALA_ARMA)


#Shuriken
imagen_balas = pygame.image.load(f"assets//images//weapons//01.png").convert_alpha()
imagen_balas = escalar_img(imagen_balas, constantes.SCALA_ARMA)


player_image = pygame.image.load("assets/images/characters/player/Run_0.png")
#Para scalar el Asset
player_image = escalar_img(player_image, constantes.SCALA_PERSONAJE)

#Crear un jugador de la clase Personaje
jugador = Personaje(50,50, animaciones)

#Crear un arma de la clase Weapon
shuriken = Weapon(imagen_shuriken, imagen_balas)

#Crear un grupo de sprites
grupo_balas = pygame.sprite.Group()


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

    #Actualiza el estado jugador
    jugador.update()

    #Actualizar el estado del arma
    bala = shuriken.update(jugador)
    if bala:
        grupo_balas.add(bala)
    for bala in grupo_balas:
        bala.update()

    #print(grupo_balas)

    #Dibujar al jugador
    jugador.dibujar(ventana)

    #Dibujar el arma
    shuriken.dibujar(ventana)

    #Dibujar balas
    for bala in grupo_balas:
        bala.dibujar(ventana)

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