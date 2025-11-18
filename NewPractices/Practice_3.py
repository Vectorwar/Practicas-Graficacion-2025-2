import pygame
pygame.init()
pygame.mixer.init()
pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Práctica 3 - Disparos")
x, y = 50, 300
balas = []
clock = pygame.time.Clock()
running = True

sonido = pygame.mixer.Sound(r"C:\Users\ThinkPad\OneDrive\Desktop\Practicas-Graficacion-2025-2\NewPractices\disparo.mp3")


while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                balas.append([pygame.Rect(x + 40, y + 15, 10, 5), 15, 0])
                if sonido:
                    sonido.play()
            
            elif event.key == pygame.K_w:
                # Up bullets
                balas.append([pygame.Rect(x + 15, y, 5, 10), 0, -15])
                if sonido:
                    sonido.play()
            
            elif event.key == pygame.K_s:
                # Down bullets
                balas.append([pygame.Rect(x + 15, y + 40, 5, 10), 0, 15])
                if sonido:
                    sonido.play()
    
    #movement of bullets
    for bala in balas:
        bala[0].x += bala[1]
        bala[0].y += bala[2]
    
    #bullets delete
    balas = [b for b in balas if 0 <= b[0].x <= 600 and 0 <= b[0].y <= 400]
    
    pantalla.fill((20, 20, 20))
    pygame.draw.rect(pantalla, (0, 255, 0), (x, y, 40, 40))
    
    for b in balas:
        pygame.draw.rect(pantalla, (255, 0, 0), b[0]) 
    
    pygame.display.update()
pygame.quit()