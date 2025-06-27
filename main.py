import pygame

import constantes
from personaje import Personaje
from weapon import Weapon
import os
from textos import DamageText

#Funciones

#Escalar imagen



pygame.init()

#Variables de ventana
#ancho = 800
#alto = 600

ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA,
                                   constantes.ALTO_VENTANA))

#Cambiar el nombre de la ventana
pygame.display.set_caption("Mi primer juego")

#Fuentes
font = pygame.font.Font("assets//fonts//monogram.ttf", 25)


def escalar_img(image, scale):
    w = image.get_width()
    h = image.get_height()
    nueva_imagen = pygame.transform.scale(image, (w*scale, h*scale))
    return nueva_imagen

#Función contar elementos
def contar_elementos(directorio):
    return len(os.listdir(directorio))
#print(os.listdir("assets/images/characters/enemies/demon"))


#Listar nombre elementos
def nombres_carpetas(directorio):
    return os.listdir(directorio)
#print(nombres_carpetas("assets/images/characters/enemies"))



#Importar imagenes

#Personaje
animaciones = []
for i in range (8):
    img = pygame.image.load(f"assets//images//characters//player//Run_{i}.png").convert_alpha()
    ima = escalar_img(img, constantes.SCALA_PERSONAJE)
    animaciones.append(img)

#enemies
#Contar enemigos
directorio_enemigos = "assets//images//characters//enemies"
tipo_enemigos = nombres_carpetas(directorio_enemigos)
#print(f"enemigos:{tipo_enemigos}")


animaciones_enemigos = []
for eni in tipo_enemigos:
    lista_temp = []
    ruta_temp = f"assets//images//characters//enemies//{eni}"
    num_animaciones = contar_elementos(ruta_temp)
    #print (f"número de img: {num_animaciones}")

    for i in range(num_animaciones):
        img_enemigo = pygame.image.load(f"{ruta_temp}//{eni}_{i+1}.png").convert_alpha()
        img_enemigo = escalar_img(img_enemigo, constantes.SCALA_ENEMIGOS)
        lista_temp.append(img_enemigo)
    animaciones_enemigos.append(lista_temp)
#print(animaciones_enemigos)


#print(tipo_enemigos)

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
jugador = Personaje(50,50, animaciones, 100)

#Crear un enemigo de la clase Personaje
demon = Personaje(200, 200, animaciones_enemigos[0], 100)
demon_2 = Personaje(400, 400, animaciones_enemigos[0], 100)
freezer = Personaje(40, 40, animaciones_enemigos[1], 200)

#Crear lista de enemigos
lista_enemigos = []
lista_enemigos.append(demon)
lista_enemigos.append(demon_2)
lista_enemigos.append(freezer)
#print(lista_enemigos)


#Crear un arma de la clase Weapon
shuriken = Weapon(imagen_shuriken, imagen_balas)

#Crear un grupo de sprites
grupo_damage_text = pygame.sprite.Group()
grupo_balas = pygame.sprite.Group()

#temporal y borrar
#damage_text = DamageText(100, 240, "25", font, constantes.ROJO)
#grupo_damage_text.add(damage_text)

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

    #Actualiza el estado del enemigo
    for ene in lista_enemigos:
        ene.update()
        print (ene.energia)

    #Actualizar el estado del arma
    bala = shuriken.update(jugador)
    if bala:
        grupo_balas.add(bala)
    for bala in grupo_balas:
        damage, pos_damage = bala.update(lista_enemigos)
        if damage:
            damage_text = DamageText(pos_damage.centerx, pos_damage.centery, str(damage), font, constantes.ROJO)
            grupo_damage_text.add(damage_text)

    #Actualizar daño
    grupo_damage_text.update()

    #print(grupo_balas)

    #Dibujar al jugador
    jugador.dibujar(ventana)

    #Dibujar al enemigo
    for ene in lista_enemigos:
        ene.dibujar(ventana)

    #Dibujar el arma
    shuriken.dibujar(ventana)

    #Dibujar balas
    for bala in grupo_balas:
        bala.dibujar(ventana)

    #Dibujar textos
    grupo_damage_text.draw(ventana)

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