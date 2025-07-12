import pygame
import constantes
from personaje import Personaje
from weapon import Weapon
from textos import DamageText
from items import Item
from mundo import Mundo
import os
import csv

#Funciones

#Escalar imagen

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

pygame.init()

#Variables de ventana
#ancho = 800
#alto = 600

ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA,
                                   constantes.ALTO_VENTANA))

#Cambiar el nombre de la ventana
pygame.display.set_caption("Mi primer juego")

#Variables
posicion_pantalla = [0,0]
nivel = 1

#Fuentes
font = pygame.font.Font("assets//fonts//monogram.ttf", 25)
font_game_over = pygame.font.Font("assets//fonts//monogram.ttf", 100)
font_reinicio = pygame.font.Font("assets//fonts//monogram.ttf", 30)
font_inicio = pygame.font.Font("assets//fonts//monogram.ttf", 30)
font_titulo = pygame.font.Font("assets//fonts//monogram.ttf", 30)

game_over_text = font_game_over.render('Game Over', True, constantes.BLANCO)

texto_boton_reinicio = font_reinicio.render("Reiniciar", True, constantes.NEGRO)

boton_jugar = pygame.Rect(constantes.ANCHO_VENTANA/2-100,
                          constantes.ALTO_VENTANA/2-50, 200, 50)

boton_salir = pygame.Rect(constantes.ANCHO_VENTANA/2-100,
                          constantes.ALTO_VENTANA/2-50, 200, 50)

texto_boton_jugar = font_inicio.render("Jugar", True, constantes.NEGRO)
texto_boton_salir = font_inicio.render("Salir", True, constantes.BLANCO)

"""""
def pantalla_inicio():
    ventana.fill(constantes.COLOR_BG)
    dibujar_texto("Mi primer juego", font_titulo, constantes.BLANCO,
                  constantes.ANCHO_VENTANA/2-200,
                  constantes.ALTO_VENTANA/2-200)
    pygame.draw.rect(ventana, constantes.AMARILLO, boton_jugar)
    pygame.draw.rect(ventana, constantes.ROJO, boton_salir)
    ventana.blit(texto_boton_jugar, (boton_jugar.x+50, boton_jugar.y+10))
    ventana.blit(texto_boton_salir, (boton_salir.x + 50, boton_salir.y + 10))
    pygame.display.update()
"""""
#Importar imagenes
#Energía
corazon_vacio = pygame.image.load("assets//images//items//Heart_3.png").convert_alpha()
corazon_vacio = escalar_img(corazon_vacio, constantes.SCALA_CORAZON)
corazon_mitad = pygame.image.load("assets//images//items//Heart_2.png").convert_alpha()
corazon_mitad = escalar_img(corazon_mitad, constantes.SCALA_CORAZON)
corazon_lleno = pygame.image.load("assets//images//items//Heart_1.png").convert_alpha()
corazon_lleno = escalar_img(corazon_lleno, constantes.SCALA_CORAZON)

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

#Cargar imagenes del mundo
tile_list = []
for x in range(constantes.TILE_TYPES):
    tile_image = pygame.image.load(f"assets//images//tiles//Rock_{x + 1}.png")
    tile_image = pygame.transform.scale(tile_image, (constantes.TILE_SIZE, constantes.TILE_SIZE))
    tile_list.append(tile_image)

#Cargar imagen de los items
pocion_turquesa = pygame.image.load("assets/images/items/Potion.png")
pocion_turquesa = escalar_img(pocion_turquesa, 1)

coin_images = []
ruta_img = "assets//images//items//coin"
num_coin_images = contar_elementos(ruta_img)
#print (f"número de imagenes de monedas: {num_coin_images}")
for i in range(num_coin_images):
    img = pygame.image.load(f"assets//images//items//coin//coin_{i+1}.png")
    img = escalar_img(img, 1)
    coin_images.append(img)

def dibujar_texto(texto, fuente, color, x, y):
    img = fuente.render(texto, True, color)
    ventana.blit(img, (x, y))

player_image = pygame.image.load("assets/images/characters/player/Run_0.png")
#Para scalar el Asset
player_image = escalar_img(player_image, constantes.SCALA_PERSONAJE)

def vida_jugador():
    c_mitad_dibujado = False
    for i in range(4):
        if jugador.energia >= ((i+1)*25):
            ventana.blit(corazon_lleno, (5+i*50,5))
        elif jugador.energia % 25 > 0 and c_mitad_dibujado == False:
            ventana.blit(corazon_mitad,(5+i*50,5))
            c_mitad_dibujado = True
        else:
            ventana.blit(corazon_vacio, (5+i*50,5))

world_data = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

"""""
for fila in range(constantes.FILAS):
    filas = [5] * constantes.COLUMNAS
    world_data.append(filas)

#cargar el archivo con el nivel
with open("niveles//dungeon.csv", newline=' ') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for x, fila in enumerate(reader):
        for y, columna in enumerate(fila):
            world_data[x][y] = int(columna)
"""""

world = Mundo()
world.process_data(world_data, tile_list)


def dibujar_grid():
    for x in range(30):
        pygame.draw.line(ventana, constantes.BLANCO, (x*constantes.TILE_SIZE, 0),(x*constantes.TILE_SIZE, constantes.ALTO_VENTANA))
        pygame.draw.line(ventana, constantes.BLANCO, (0, x * constantes.TILE_SIZE), (constantes.ANCHO_VENTANA, x*constantes.TILE_SIZE))

#Crear un jugador de la clase Personaje
jugador = Personaje(10,10, animaciones, 70, 1)

#Crear un enemigo de la clase Personaje
demon = Personaje(200, 200, animaciones_enemigos[0], 100, 2)
demon_2 = Personaje(400, 400, animaciones_enemigos[0], 100, 2)
freezer = Personaje(300, 100, animaciones_enemigos[1], 200, 2)


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
grupo_items = pygame.sprite.Group()

coin = Item(350, 350, 0, coin_images)
coin_1 = Item(550, 250, 0, coin_images)
potion = Item(380, 500, 1, [pocion_turquesa])
potion_1 = Item(470, 230, 1, [pocion_turquesa])

grupo_items.add(coin, coin_1)
grupo_items.add(potion, potion_1)


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


mostrar_inicio = True
#Variable
run = True

#LOOP para mantener la ventana abierta
while run:

        #60 FPS Frame Rate
    reloj.tick(constantes.FPS)

    ventana.fill(constantes.COLOR_BG)

    if jugador.vivo:


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
        posicion_pantalla = jugador.movimiento(delta_x, delta_y)
        print (posicion_pantalla)

        world.update(posicion_pantalla)

            #Actualiza el estado jugador
        jugador.update()

            #Actualiza el estado del enemigo
        for ene in lista_enemigos:
            ene.update()
                #print (ene.energia)

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
        grupo_damage_text.update(posicion_pantalla)

            #Actualizar items
        grupo_items.update(posicion_pantalla, jugador)

        #Dibujar mundo
    world.draw(ventana)

        #print(grupo_balas)

        #Dibujar al jugador
    jugador.dibujar(ventana)

        #Dibujar al enemigos
    for ene in lista_enemigos:
        if ene.energia == 0:
            lista_enemigos.remove(ene)
        if ene.energia > 0:
            ene.enemigos(jugador, posicion_pantalla)
            ene.dibujar(ventana)

        #Dibujar el arma
    shuriken.dibujar(ventana)

        #Dibujar balas
    for bala in grupo_balas:
        bala.dibujar(ventana)

        #Dibujar los corazones
    vida_jugador()

        #Dibujar textos
    grupo_damage_text.draw(ventana)
    dibujar_texto(f"Score: {jugador.score}", font, (255,255,0), 700, 5)
        #nivel
    dibujar_texto(f"Nivel: " + str(nivel), font, constantes.BLANCO, constantes.ANCHO_VENTANA/2, 5)

        # dibujar items
    grupo_items.draw(ventana)

    if jugador.vivo == False:
        ventana.fill(constantes.ROJO_OSCURO)
        text_rect = game_over_text.get_rect(center = (constantes.ANCHO_VENTANA/2,
                                                          constantes.ALTO_VENTANA/2))
        ventana.blit(game_over_text, text_rect)

        boton_reinicio = pygame.Rect(constantes.ANCHO_VENTANA/2-100,
                                         constantes.ALTO_VENTANA/2+100, 200, 50)
        pygame.draw.rect(ventana, constantes.AMARILLO, boton_reinicio)
        ventana.blit(texto_boton_reinicio,
                         (boton_reinicio.x+50, boton_reinicio.y + 10))

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

        if event.type == pygame.MOUSEBUTTONDOWN:
            if boton_reinicio.collidepoint(event.pos) and not jugador.vivo:
                jugador.vivo = True
                jugador.energia = 100
                jugador.score = 0
                nivel = 1
                world = Mundo()
                world.process_data(world_data, tile_list)
                lista_enemigos = []
                demon = Personaje(200, 200, animaciones_enemigos[0], 100, 2)
                demon_2 = Personaje(400, 400, animaciones_enemigos[0], 100, 2)
                freezer = Personaje(300, 100, animaciones_enemigos[1], 200, 2)
                lista_enemigos.append(demon)
                lista_enemigos.append(demon_2)
                lista_enemigos.append(freezer)

        #Para actualizar la ventana
    pygame.display.update()

pygame.quit()