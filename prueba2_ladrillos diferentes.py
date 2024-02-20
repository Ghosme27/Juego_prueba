import pygame
from random import randint
import ladrillo

# Comienzo de la extensión pygame
pygame.init()

# Creacion de la pantalla de la superficie
window = pygame.display.set_mode((800, 600))  # Aqui tenemos las dimensiones que tiene nuestra ventana de juego
pygame.display.set_caption('Arkanoid_Prueba')

# Creacion de la pelota de juego
ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()
speed = [randint(3, 6), randint(3, 6)]
ballrect.move_ip(400, 300)

# Creamos una barra para nuestro juego para el rebote con nuestro pelota y su rectangulo
barra = pygame.image.load("barra_nuevo.png")
barrarect = barra.get_rect()
barrarect.move_ip(300, 550)

# Hacemos una lista con los ladrillos
lista_ladrillos = []
for posx in range(13):
    for posy in range(4):
        ladrillo_obj = ladrillo.LAD_AZUL(25 * posx, 25 * posy, 'lad.azul.png')
        lista_ladrillos.append(ladrillo_obj)

# Bucle principal del arkonaid
jugar = True
while jugar:  # esto hara que mientras jugar sea true este en funcionamiento
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugar = False  # Con esto el bucle ira comporbando si el boton de la ventana esta abierto si no es asi se cerrara y se quitara el juego.

    # Comprobacion del pulsamiento de una tecla para su movimiento
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:  # movimiento para la izquierda y cuanto se mueve
        barrarect = barrarect.move(-2, 0)
    if keys[pygame.K_RIGHT]:  # movimiento para la derecha y cuanto se mueve
        barrarect = barrarect.move(2, 0)

    # Comprobación de colisiones pelota - ladrillo
    for ladrillo_obj in lista_ladrillos:
        window.blit(ladrillo_obj.image, ladrillo_obj.rect)
        # Colisiones pelota - ladrillo
        if ballrect.colliderect(ladrillo_obj.rect):
            lista_ladrillos.remove(ladrillo_obj)
            speed[1] = -speed[1]

    # Movimiento de la pelota
    ballrect = ballrect.move(speed)

    # Límite para nuestra barra y no se escape de la pantalla
    # Pondremos un comprobador para cuando choque la pelota a los limites de la pantalla o cuando choque con la barra
    if barrarect.colliderect(ballrect):  # comprueba si los hitboxs chocan
        speed[1] = -speed[1]
    if ballrect.left < 0 or ballrect.right > window.get_width():
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > window.get_height():
        speed[1] = -speed[1]

    # Pintaremos la ventana de juego de un color que nosotros queramos dentro del bucle lo haremos.
    window.fill((3, 100, 100))
    # dibujamos la pelota y la barra
    window.blit(barra, barrarect)
    window.blit(ball, ballrect)
    # Los elementos del juego se redibujan.
    pygame.display.flip()
    # Para tener una tasa de refresco(FPS)
    pygame.time.Clock().tick(60)

pygame.quit()


