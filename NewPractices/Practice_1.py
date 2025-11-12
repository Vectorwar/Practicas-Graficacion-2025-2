"""Practica 1: Movimiento basico"""
import pygame 

pygame.init()
pygame.display.set_caption("Practica 1: Movimiento basico")
width, height = 800, 600
screen = pygame.display.set_mode((width, height)) 


#colors for use in the game
BLACK = (30, 30, 30)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

#player properties
player_size = 30

x,  y = 300, 200 
vel = 5
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel
    if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]: #Velocity boost 
        vel = 10
    else:
        vel = 5
    
    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, (x, y, player_size, player_size))
    pygame.display.update()

pygame.quit()