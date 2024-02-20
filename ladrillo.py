import pygame

class LAD_AZUL():
    def __init__(self, pos_x, pos_y, picture):
         self.__image = pygame.image.load(picture)
         self.__rect = self.__image.get_rect()
         self.__rect.move_ip(pos_x, pos_y)

    @property
    def rect(self):
        return self.__rect

    @property
    def image(self):
        return self.__image

    def move(self, posi_x, posi_y):
        self.__rect.move_ip(posi_x, posi_y)
    
