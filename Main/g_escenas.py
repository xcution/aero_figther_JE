__author__ = 'eriasu'
#Imports
import pygame
from Config import Pantalla
#-------
#Clases
class Director():
    def __init__(self,titulo=""):
        pygame.init()
        self.pantalla = pygame.display.set_mode(Pantalla)
        pygame.display.set_caption(titulo)
        self.escena = None
        self.reloj = pygame.time.Clock()
    def ejecutar(self,escena_inicial,fps=60):
        self.escena = escena_inicial
        jugando = True
        while jugando:
            self.reloj.tick(fps)
            eventos = pygame.event.get()
            for evento in eventos:
                if evento.type==pygame.QUIT:
                    jugando=False
                elif evento.type==pygame.KEYDOWN:
                    if evento.key==pygame.K_ESCAPE:
                        jugando = False
            self.escena.leer_eventos(eventos)
            self.escena.actualizar()
            self.escena.dibujar(self.pantalla)
            self.escena=self.escena.escena
            pygame.display.flip()
class Escena:
    def __init__(self):
        self.escena = self
    def leer_eventos(self,eventos):
        pass
    def actualizar(self):
        pass
    def dibujar(self,pantalla):
        pass
    def cambiar_escena(self,escena):
        self.escena=escena
#------