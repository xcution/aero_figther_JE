__author__ = 'eriasu'
import pygame
from Comun import Width,Height,Pantalla,load_image,Texto,musica
from g_escenas import Escena
from Objects import Jugador
class Escena_Inicial(Escena):
    def __init__(self):
        Escena.__init__(self)
        self.fondo=load_image('fondo_tem.png')
        self.reiniciar=Texto("[Enter] Iniciar Juego Nuevo",tamano=36)
        self.musica=musica("Dethklok-The Galaxy.flac")
        self.musica.cargar_musica()
    def leer_eventos(self,eventos):
        for evento in eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key==pygame.K_RETURN:
                    self.musica.detener_musica()
                    self.cambiar_escena(Escena_Juego())
    def dibujar(self,pantalla):
        pantalla.blit(self.fondo,(0,0))
        pantalla.blit(self.reiniciar.mostrar(),(10, Height-self.reiniciar.rect.h-10))
class Escena_Juego(Escena):
    def __init__(self):
        Escena.__init__(self)
        self.fondo=load_image('fondo.png')
        self.jugador=Jugador()
        self.puntos=0
        self.puntuacion=Texto("Puntos: ")
        pygame.key.set_repeat(1,25)
    def leer_eventos(self,eventos):
        for evento in eventos:
            if evento.type==pygame.KEYDOWN:
                self.jugador.mover(evento.key)
                self.jugador.atacar(evento.key)

    def actualizar(self):
       pass
    def dibujar(self,pantalla):
        pantalla.blit(self.fondo,(0,0))
        pantalla.blit(self.puntuacion.mostrar(str(self.puntos)),(0,0))
        pantalla.blit(self.jugador.imagen,self.jugador.rect)

class Escena_Juego_Terminado(Escena):
    pass