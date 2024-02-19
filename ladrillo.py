import pygame

class ladrillo1():
    def _init_(self, pos_x, pos_y, picture):
        self._image = pygame.image.load(picture)
        self._rect = self.image.get_rect()
        self._rect.move_ip(pos_x, pos_y)
    @property
    def rect(self):
        return self._rect
    @property
    def picture(self):
        return self._image
    
    def move(self,posi_x,posi_y):
        self._rect.move(posi_x,posi_y)

