import pygame
from pygame.examples.cursors import image

import constantes


class Personaje():
    def __init__(self, x, y, animaciones, energia):
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

    def movimiento (self, delta_x, delta_y):

       #Para Voltear el Asset
        if delta_x < 0:
            self.flip = True
        if delta_x > 0:
            self.flip = False

        self.forma.x = self.forma.x + delta_x
        self.forma.y = self.forma.y + delta_y

    #Metodo en milisegundos de cooldown
    def update(self):
        #Comprobar si el personaje ha muerto
        if self.energia <= 0:
            self.energia = 0
            self.vivo = False

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