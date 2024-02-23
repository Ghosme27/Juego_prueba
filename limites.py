import pygame

class limites_pantalla:
    def __init__(self,game):
        self.game = game
    
    def dibuja_limites(self):
        pygame.draw.rect(self.game.pantalla,self.game.GRIS2, (51,21,919,9))
        pygame.draw.rect(self.game.pantalla,(5,5,5), (60,29,900,1))
        pygame.draw.rect(self.game.pantalla,(250,250,250),(51,21,919,2))

        pygame.draw.rect(self.game.pantalla,self.game.GRIS2, (51,21,9,630))
        pygame.draw.rect(self.game.pantalla,(5,5,5), (59,29,1,630))
        pygame.draw.rect(self.game.pantalla,(250,250,250),(51,21,2,639))

        pygame.draw.rect(self.game.pantalla,self.game.GRIS2, (960,29,9,630))
        pygame.draw.rect(self.game.pantalla,(5,5,5), (960,29,1,630))
        pygame.draw.rect(self.game.pantalla,(250,250,250),(968,21,2,639))
        

