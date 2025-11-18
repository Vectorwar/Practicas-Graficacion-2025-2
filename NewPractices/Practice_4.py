import pygame
import random
pygame.init()

pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Práctica 4 - Colisiones")

jugador = pygame.Rect(50, 300, 40, 40)
balas = []
enemigos = [pygame.Rect(500, 300, 40, 40)]
clock = pygame.time.Clock()
running = True
puntos = 0
fuente = pygame.font.Font(None,36)


while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            balas.append(pygame.Rect(jugador.x + 40, jugador.y + 15, 10, 5))
    #movement of player
        teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        jugador.x -= 5
    if teclas[pygame.K_RIGHT]:
        jugador.x += 5
    if teclas[pygame.K_UP]:
        jugador.y -= 5
    if teclas[pygame.K_DOWN]:
        jugador.y += 5

    for b in balas:
        b.x += 10
    balas = [b for b in balas if b.x < 600]

    for b in balas[:]:
        for e in enemigos[:]:
            if b.colliderect(e):
                balas.remove(b)
                enemigos.remove(e)
                puntos += 10
                nuevo_x = random.randint(400, 550)
                nuevo_y = random.randint(50, 350)
                enemigos.append(pygame.Rect(nuevo_x, nuevo_y,40, 40))
                break

    pantalla.fill((0, 0, 0))
    pygame.draw.rect(pantalla, (0, 255, 0), jugador)
    for b in balas:
        pygame.draw.rect(pantalla, (255, 255, 0), b)
    for e in enemigos:
        pygame.draw.rect(pantalla, (255, 0, 0), e)
    
    text_puntos = fuente.render(f"Puntos:{puntos}", True, (255, 255, 255))
    pantalla.blit(text_puntos, (10, 10))

    pygame.display.update()

pygame.quit()
