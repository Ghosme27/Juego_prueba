import pygame
#Comienzo de la extension pygame
pygame.init()

#Creacion de la pantalla de la superficie
window = pygame.display.set_mode((800,600))#Aqui tenemos las dimensiones que tiene nuestra ventana de juego
pygame.display.set_caption('Arkanoid_Prueba')

#Creacion de la pelota de juego
ball = pygame.image.load("ball_nuevo.png")

#Tener el rectángulo de la imagen utilizada
ballrect = ball.get_rect()

#Pondremos unos valores que tendra la velocidad inicial nuestra pelota
speed = [4,4]

#Posicion inicial de nuestra pelota que sera en el origen de coordenandas
ballrect.move_ip(0,0)

#Bucle principal del arkonaid
jugar = True 
while jugar: #esto hara que mientras jugar sea true este en funcionamiento
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugar = False #Con esto el bucle ira comporbando si el boton de la ventana esta abierto si no es asi se cerrara y se quitara el juego.
    #movimiento de la pelota
    ballrect = ballrect.move(speed)
    #Pondremos un comprobador para cuando choque la pelota a los limites de la pantalla
    if ballrect.left < 0 or ballrect.right > window.get_width():
        speed [0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > window.get_height():
        speed [1] = -speed[1]
    #Pintaremos la ventana de juego de un color que nosotros queramos dentro del bucle lo haremos.
    window.fill((3,100,100))
    #dibujamos la pelota
    window.blit(ball,ballrect)
    #Los elemntos del juego se redibujan.
    pygame.display.flip()
    #Para tener una tasa de refresco(FPS)
    pygame.time.Clock().tick(60)
    
pygame.quit()

