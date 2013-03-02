__author__ = 'eriasu'
import pygame
from Config import Width,Height,Pantalla,load_image,Texto,cargar_musica
from g_escenas import Escena
class Escena_Inicial(Escena):
    def __init__(self):
        Escena.__init__(self)
        self.fondo=load_image('inicial.jpg')
        self.reiniciar=Texto("[Enter] Iniciar Juego Nuevo",tamano=36)
        self.musica=cargar_musica("Dethklok-The Galaxy.flac")
    def leer_eventos(self,eventos):
        for evento in eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key==pygame.K_RETURN:
                    print evento.key()
                    #self.cambiar_escena(Escena_Juego())
    def dibujar(self,pantalla):
        pantalla.blit(self.fondo,(0,0))
        pantalla.blit(self.reiniciar.mostrar(),(10, Height-self.reiniciar.rect.h-10))
class Escena_Juego(Escena):
    def __init__(self):
        Escena.__init__(self)


class Escena_Juego_Terminado(Escena):
    pass