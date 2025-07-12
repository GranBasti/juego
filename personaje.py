import pygame
import constantes
import math

class Personaje():
    def __init__(self, x, y, animaciones, energia, tipo):
        self.score = 0
        self.energia = energia
        self.vivo = True
        self.flip = False #Para voltear al jugador
        self.animaciones = animaciones

        #Imagen de la animación que se está mostrando actualmente
        self.frame_index = 0
        self.image = animaciones[self.frame_index]
        #Aquí se almacena la hora actual (en milisegundos que se inicio 'pygame')
        self.update_time = pygame.time.get_ticks()
        self.forma = self.image.get_rect()
        self.forma.center = (x,y)
        self.tipo = tipo
        self.golpe = False
        self.ultimo_golpe = pygame.time.get_ticks()
        self.golpe = False
        self.ultimo_golpe = pygame.time.get_ticks()


    def movimiento (self, delta_x, delta_y):
        posicion_pantalla = [0,0]
        nivel_completado = False

       #Para Voltear el Asset
        if delta_x < 0:
            self.flip = True
        if delta_x > 0:
            self.flip = False

        self.forma.x = self.forma.x + delta_x
        self.forma.y = self.forma.y + delta_y

        #Lógica solo aplica al jugador y no enemigos
        if self.tipo == 1:
            #Actualizar la pantalla basada la posición del jugador
            #Mover la cámara izquierda a derecha
            if self.forma.right > (constantes.ANCHO_VENTANA - constantes.LIMITE_PANTALLA):
                posicion_pantalla[0] = (constantes.ANCHO_VENTANA - constantes.LIMITE_PANTALLA) - self.forma.right
                self.forma.right = constantes.ANCHO_VENTANA - constantes.LIMITE_PANTALLA
            if self.forma.left < constantes.LIMITE_PANTALLA:
                posicion_pantalla[0] = constantes.LIMITE_PANTALLA - self.forma.left
                self.forma.left = constantes.LIMITE_PANTALLA

            if self.forma.bottom > (constantes.ALTO_VENTANA - constantes.LIMITE_PANTALLA):
                posicion_pantalla[1] = (constantes.ALTO_VENTANA - constantes.LIMITE_PANTALLA) - self.forma.bottom
                self.forma.bottom = constantes.ALTO_VENTANA - constantes.LIMITE_PANTALLA
            if self.forma.top < constantes.LIMITE_PANTALLA:
                posicion_pantalla[1] = constantes.LIMITE_PANTALLA - self.forma.top
                self.forma.top = constantes.LIMITE_PANTALLA
        return posicion_pantalla

    def enemigos (self, jugador, posicion_pantalla):
        ene_dx = 0
        ene_dy = 0

        #Reposicion de enemigos basado en la posición de la pantalla o c´mara
        self.forma.x += posicion_pantalla[0]
        self.forma.y += posicion_pantalla[1]

        #Distancia con el jugador
        distancia = math.sqrt(((self.forma.centerx - jugador.forma.centerx)**2) +
                        ((self.forma.centery - jugador.forma.centery)**2))
        if distancia < constantes.RANGO:
            if self.forma.centerx > jugador.forma.centerx:
                ene_dx = -constantes.VELOCIDAD_ENEMIGO
            if self.forma.centerx < jugador.forma.centerx:
                ene_dx = constantes.VELOCIDAD_ENEMIGO
            if self.forma.centery > jugador.forma.centery:
                ene_dy = -constantes.VELOCIDAD_ENEMIGO
            if self.forma.centery < jugador.forma.centery:
                ene_dy = constantes.VELOCIDAD_ENEMIGO
        self.movimiento(ene_dx,ene_dy)

        #Atacar al jugador
        if distancia < constantes.RANGO_ATAQUE and jugador.golpe == False:
            jugador.energia -= 10
            jugador.golpe = True
            jugador.ultimo_golpe = pygame.time.get_ticks()

    #Metodo en milisegundos de cooldown
    def update(self):
        #Comprobar si el personaje ha muerto
        if self.energia <= 0:
            self.energia = 0
            self.vivo = False

        #timer para poder volver a recibir daño
        golpe_cooldown = 1000
        if self.tipo == 1:
            if self.golpe == True:
                if pygame.time.get_ticks() - self.ultimo_golpe > golpe_cooldown:
                    self.golpe = False

        cooldown_animacion = 100
        self.image = self.animaciones[self.frame_index]
        if pygame.time.get_ticks() - self.update_time >=cooldown_animacion:
            self.frame_index = self.frame_index + 1
            self.update_time = pygame.time.get_ticks()
        if self.frame_index >= len(self.animaciones):
            self.frame_index = 0

    def dibujar(self, interfaz):
        imagen_flip = pygame.transform.flip(self.image, self.flip, False)
        interfaz.blit(imagen_flip, self.forma)

        #pygame.draw.rect(interfaz, constantes.COLOR_PERSONAJE, self.forma, 1)