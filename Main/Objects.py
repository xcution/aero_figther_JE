__author__ = 'eriasu'
import pygame
from Comun import Width,Height,load_image
class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagen = load_image("navefrente.png",alpha=True)
        self.rect=self.imagen.get_rect()
        self.rect.centerx=Width/2
        self.rect.centery=Height-40
        self.speed=[3,3]

    def mover(self,tecla):
        if tecla ==pygame.K_LEFT:
            self.speed=[-15,0]
        elif tecla==pygame.K_RIGHT:
            self.speed=[15,0]
        elif  tecla==pygame.K_UP:
            self.speed=[0,-15]
        elif tecla==pygame.K_DOWN:
            self.speed=[0,15]

        else:
            self.speed=[0,0]
        self.rect.move_ip(self.speed)
        if self.rect.left<0:
            self.rect.left=0
        if self.rect.right>Width:
            self.rect.right=Width
    def atacar(self,tecla):
        if tecla==pygame.K_x:
            self.bala=Bala(self.rect.centerx,self.rect.centery)
        elif tecla==pygame.K_c:
            print "Arma Nuclear"
class Bala(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.imagen         = load_image('bala.png',alpha=True)
        self.rect           = self.imagen.get_rect()
        self.posx           = posx
        self.posy           = posy
        self.rect.centerx   = self.posx
        self.rect.centery   = self.posy
        self.speed = [3,3]
    def mover(self):
        pass
    def colicion(self):
        pass
class enemigo(pygame.sprite.Sprite):
    def __init__(self):
        pass