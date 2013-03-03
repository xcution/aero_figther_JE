__author__ = 'eriasu'
import  pygame
from pygame.locals import  RLEACCEL
import os
#Constantes
Width  =   600
Height =   700
Pantalla = (Width,Height)
#Clases
class spritesheet(object):
    def __init__(self,nombre_imagen):
        self.sheet=load_image(nombre_imagen)
    def image_at(self,rectangle,colorkey=None):
        rect = pygame.Rect(rectangle)
        imagen = pygame.Surface(rect.size).convert()
        imagen.blit(self.sheet,(0,0),rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = imagen.get_at((0,0))
            imagen.set_colorkey(colorkey,pygame.RLEACCEL)
        return imagen
    def images_at(self,rects,colorkey=None):
        return [self.image_at(rect,colorkey) for rect in rects]
#Funciones
def load_image(filename,alpha=False,directorio="Imagenes"):
    ruta = os.path.join(directorio,filename)
    try:
        image = pygame.image.load(ruta)
    except pygame.error,message:
        raise SystemExit,message

    if alpha:
        image = image.convert_alpha()
    else:
        image= image.convert()
    return image
class Sonido():
    def __init__(self,nombre,directorio="Sonidos"):
        self.nombre=nombre
        self.directorio=directorio
    def cargar_sonido(self):
        ruta = os.path.join(self.directorio,self.nombre)
        sonido = pygame.mixer.Sound(ruta)
        sonido.play()

class musica():
    def __init__(self,nombre,directorio="musica"):
        self.nombre=nombre
        self.directorio=directorio



    def cargar_musica(self,veces_a_repetir=0):
        ruta = os.path.join(self.directorio,self.nombre)
        try:
            pygame.mixer.music.load(ruta)
        except pygame.error,message:
            raise SystemExit,message
        pygame.mixer.music.play(veces_a_repetir)
    def detener_musica(self):
        pygame.mixer.music.stop()

class Texto():
    "Crea un texto para mostrar en pantalla."
    def __init__(self, predeterminado = "", tamano = 24, fuente = None, color = (0, 0, 0)):
        self.fuente = pygame.font.Font(fuente, tamano)
        self.default = predeterminado
        self.texto = None
        self.rect = None
        self.color = color
        self.mostrar()

    def mostrar(self, cadena = ""):

        self.texto = self.fuente.render(self.default + cadena, True, self.color)
        self.rect = self.texto.get_rect()
        return self.texto
#Directorios
