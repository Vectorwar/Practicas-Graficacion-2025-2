"""Práctica 2: Saltos y gravedad"""

import pygame
pygame.init()

pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Práctica 2 - Saltos y gravedad")

#colors
BROWN = (150, 75, 0)
RED = (255, 0, 0)

x, y = 300, 300
vel_y = 0
gravedad = 1
en_suelo = True
double_jump_available = False #Variable to track double jump
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:  #detect jump key press
            if event.key == pygame.K_SPACE and en_suelo:
                vel_y = -10 # jump impulse
                en_suelo = False
                double_jump_available = True
            elif event.key == pygame.K_SPACE and not en_suelo and double_jump_available:
                vel_y = -10 # double jump impulse
                double_jump_available = False

    y += vel_y 
    vel_y += gravedad

    if y >= 300:
        y = 300
        vel_y = 0
        en_suelo = True
        double_jump_available = False # reset double jump on landing

    pantalla.fill((50, 50, 100))
    pygame.draw.rect(pantalla, (RED), (x, y, 40, 40))
    pygame.draw.rect(pantalla, (BROWN), (0, 340, 600, 60))
    pygame.display.update()

pygame.quit()