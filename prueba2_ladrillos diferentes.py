import pygame
import random
import sys
from limites import limites_pantalla
class juego:
    def __init__(self):
        pygame.init()#iniciar el juego
        pygame.mixer.init()#para poner musica en el futuro
        self.AZUL_C = (144,285,285)#colores para diferentes objetos
        self.GRIS = (67,67,67)
        self.GRIS2 = (170,170,170)
        self.GRIS_C = (120,120,120)
        self.rejugar = False
        self.gameOver = True
        self.nivel_superado = False
        self.puntos = 0
        self.nivel = 1
        resolucion = (1020,660)#Ponemos 
        self.res = resolucion

    
    def crear_lista_imagenes(self):#para los imagenes que utilizaremos en el programa
        pass

    def nuevo_juego(self): #para comenzar un nuevo juego
        pass

    def actualizar(self):
        if not self.gameOver:
            pass
        
        self.reloj.tick(self.FPS)
        pygame.display.update()

    def dibujar(self):
        self.pantalla.fill(self.GRIS_C)
        #dibujos

        if not self.gameOver:
            pass
    
    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if not self.gameOver:
                pass
                #self.palajugador = self.palajugador.leer_teclado()
            
            else:
                if event.type == pygame.KEYDOWN:
                    if pygame.K_KP_ENTER:
                        self.gameOver = False
                        self.nuevo_juego()
                        self.iniciar()
    def iniciar(self):
        while not self.gameOver:
            self.check_event()
            self.actualizar()
            self.dibujar()
        while self.gameOver:
            self.actualizar()
            self.dibujar()
            self.check_event()

if __name__ == '__main__':
    juego1 = juego()
    juego1.run()#para que inicie el juego este sera lo unico que se iniciara
