__author__ = 'eriasu'
#Imports
from g_escenas import Director
from escenas import Escena_Inicial
#-------
#Funciones
def main():
    director = Director("Aero Fighter JE")
    director.ejecutar(Escena_Inicial(),60)
#------------
if __name__=="__main__":
    main()