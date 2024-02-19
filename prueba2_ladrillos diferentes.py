import pygame
from random import randint

pygame.init()

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Arkanoid_Prueba')

ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()
speed = [randint(3, 6), randint(3, 6)]  # Velocidad inicial aleatoria
ballrect.move_ip(400, 300)

barra = pygame.image.load("barra_nuevo.png")
barrarect = barra.get_rect()
barrarect.move_ip(300, 550)

l1 = pygame.image.load("lad.azul.png")
l1rect = l1.get_rect()
l1rect.move_ip(150, 200)

jugar = True
while jugar:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugar = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        barrarect = barrarect.move(-2, 0)
    if keys[pygame.K_RIGHT]:
        barrarect = barrarect.move(2, 0)
    
    if l1rect.colliderect(ballrect):
        # Cambiar la velocidad de la pelota aleatoriamente en ambas direcciones
        speed = [randint(3, 6), randint(3, 6)]
        l1rect.x = -1000

    ballrect = ballrect.move(speed)

    if ballrect.left < 0 or ballrect.right > window.get_width():
        # Cambiar la velocidad de la pelota aleatoriamente en ambas direcciones
        speed = [randint(3, 6), randint(3, 6)]
    if ballrect.top < 0 or ballrect.bottom > window.get_height():
        # Cambiar la velocidad de la pelota aleatoriamente en ambas direcciones
        speed = [randint(3, 6), randint(3, 6)]
    if barrarect.colliderect(ballrect):
        speed[1] = -speed[1]
    if ballrect.bottom > window.get_height():
        pass

    window.fill((3, 100, 100))
    window.blit(barra, barrarect)
    window.blit(ball, ballrect)
    window.blit(l1, l1rect)
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
