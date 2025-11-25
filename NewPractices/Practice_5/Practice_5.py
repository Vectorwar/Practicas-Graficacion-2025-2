import pygame
import random

pygame.init()

# Screen
pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Simple Mini Game")

# Colors
WHITE = (255, 255, 255)
BLUE = (100, 150, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

# load images
try:
    fondo = pygame.image.load("fondo.png")
    personaje = pygame.image.load("personaje.png")
except:
    print("No se encontro la imagen mi bro.")
    pygame.quit()
    exit()

# create background function
def crear_fondo(pos_x):
    # Draw two backgrounds to create a scrolling effect
    pantalla.blit(fondo, (-(pos_x % 600), 0))
    pantalla.blit(fondo, ((600 - (pos_x % 600)), 0))

# Character variables
x = 0
y = -200
vel_y = 0
on_ground = True

#personaje size
personaje = pygame.transform.scale(personaje, (60, 60))

# Simple animation
frame = 0

# Background
fondo_x = 0

# Enemies and shots
enemies = []
shots = []

# Points
points = 0
font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()
running = True
tiempo = 0

while running:
    clock.tick(30)
    tiempo += 1
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and on_ground:
                vel_y = -12  # Jump
                on_ground = False
            if event.key == pygame.K_x:
                shots.append([x + 30, y + 15])  # Shoot
    
    # Move background
    fondo_x += 2
    crear_fondo(fondo_x)
    
    # Draw ground
    pygame.draw.rect(pantalla, (0, 200, 0), (0, 350, 600, 50))
    
    # Jump physics
    vel_y += 0.5  # Gravity
    y += vel_y
    if y >= 300:  # Ground
        y = 300
        vel_y = 0
        on_ground = True
    
    # Update animation frame
    frame += 1
    if frame >= 60:
        frame = 0 
    
    # Create enemies every 60 frames
    if tiempo % 60 == 0:
        enemies.append([600, 310])
    
    # Move and draw enemies
    for enemy in enemies[:]:
        enemy[0] -= 4
        pygame.draw.circle(pantalla, RED, (enemy[0], enemy[1]), 20)
        if enemy[0] < -20:
            enemies.remove(enemy)
    
    # Move and draw shots
    for shot in shots[:]:
        shot[0] += 8
        pygame.draw.circle(pantalla, YELLOW, (int(shot[0]), int(shot[1])), 5)
        if shot[0] > 600:
            shots.remove(shot)
    
    # Shot-enemy collisions
    for shot in shots[:]:
        for enemy in enemies[:]:
            dx = shot[0] - enemy[0]
            dy = shot[1] - enemy[1]
            if dx*dx + dy*dy < 625:  # 25*25 (radius)
                if shot in shots:
                    shots.remove(shot)
                if enemy in enemies:
                    enemies.remove(enemy)
                points += 10
    
    # Player-enemy collision
    for enemy in enemies[:]:
        if abs(x - enemy[0]) < 40 and abs(y - enemy[1]) < 40:
            running = False  # Game Over
    
    # Draw character (image) - IMPORTANT: must be after background
    pantalla.blit(personaje, (x + 30, y + 15))
    
    # Show points
    texto = font.render(f"Points: {points}", True, WHITE)
    pantalla.blit(texto, (10, 10))
    
    # Instructions
    fuente_chica = pygame.font.Font(None, 24)
    inst = fuente_chica.render("SPACE: Jump | X: Shoot", True, WHITE)
    pantalla.blit(inst, (300, 10))
    
    pygame.display.update()

pygame.quit()