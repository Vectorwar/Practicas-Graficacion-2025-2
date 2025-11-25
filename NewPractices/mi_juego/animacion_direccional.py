import pygame
pygame.init()

# --- Configuración ---
ANCHO, ALTO = 800, 600
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Animación Direccional Completa - Sprite Sheet")

# --- Cargar imágenes ---
# Intentar cargar sprite sheet del personaje
try:
    sprite_sheet = pygame.image.load("personaje_direcciones.png").convert_alpha()
    usando_placeholder = False
except:
    # Crear sprite sheet de placeholder con 6 filas (4 direcciones + idle + ataque)
    sprite_sheet = pygame.Surface((256, 384))
    sprite_sheet.fill((255, 255, 255))
    usando_placeholder = True
    
    # Dibujar cuadros de colores para cada dirección
    colores = [
        (255, 100, 100),   # Rojo
        (100, 255, 100),   # Verde
        (100, 100, 255),   # Azul
        (255, 255, 100),   # Amarillo
        (200, 100, 200),   # Morado
        (255, 150, 0)      # Naranja
    ]
    for fila in range(6):
        for col in range(4):
            color = colores[fila]
            pygame.draw.rect(sprite_sheet, color, 
                           (col * 64, fila * 64, 64, 64))
            pygame.draw.circle(sprite_sheet, (0, 0, 0),
                             (col * 64 + 32, fila * 64 + 20), 8)
            pygame.draw.rect(sprite_sheet, (0, 0, 0),
                           (col * 64 + 24, fila * 64 + 28, 16, 24))

# intentar cargar imagen de fondo
try:
    fondo_original = pygame.image.load("fondo.png").convert()
    fondo = pygame.transform.scale(fondo_original, (ANCHO, ALTO))
    usando_fondo = True
    print("✓ Fondo 'fondo.png' cargado correctamente")
except FileNotFoundError:
    print("⚠ No se encontró 'fondo.png', usando fondo generado")
    fondo = pygame.Surface((ANCHO, ALTO))
    
    # colores del cielo con degradado
    for i in range(ALTO - 150):
        color_r = 90
        color_g = int(150 + (i / (ALTO - 150)) * 50)
        color_b = 255
        pygame.draw.line(fondo, (color_r, color_g, color_b), (0, i), (ANCHO, i))
    
    # cespe y suelo
    pygame.draw.rect(fondo, (100, 200, 100), (0, ALTO - 150, ANCHO, 150))
    # Detalles de césped
    for i in range(0, ANCHO, 20):
        pygame.draw.rect(fondo, (90, 180, 90), (i, ALTO - 150, 10, 150))
    
    # sol
    pygame.draw.circle(fondo, (255, 255, 100), (700, 80), 40)
    pygame.draw.circle(fondo, (255, 255, 150), (700, 80), 35)
    
    # nubes mejoradas
    nubes = [(100, 60), (300, 90), (500, 70), (650, 100)]
    for nx, ny in nubes:
        pygame.draw.ellipse(fondo, (255, 255, 255), (nx, ny, 120, 50)) # Cuerpo principal
        pygame.draw.ellipse(fondo, (255, 255, 255), (nx + 30, ny - 15, 80, 50)) # Parte superior
        pygame.draw.ellipse(fondo, (255, 255, 255), (nx + 60, ny, 100, 45)) # Parte inferior
    
    # montañas al fondo
    pygame.draw.polygon(fondo, (100, 150, 100), [(0, ALTO-150), (150, ALTO-250), (300, ALTO-150)])
    pygame.draw.polygon(fondo, (80, 130, 80), [(200, ALTO-150), (350, ALTO-280), (500, ALTO-150)])
    
    # arboles del fondo
    arboles = [(650, 350), (100, 380), (730, 370)]
    for ax, ay in arboles:
        pygame.draw.rect(fondo, (101, 67, 33), (ax, ay, 40, 100))
        pygame.draw.circle(fondo, (34, 139, 34), (ax + 20, ay - 10), 50)
        pygame.draw.circle(fondo, (40, 160, 40), (ax + 20, ay - 10), 40)
    
    # Camino
    pygame.draw.ellipse(fondo, (160, 140, 100), (250, ALTO - 100, 300, 80))
    
    usando_fondo = False
except Exception as e:
    print(f"⚠ Error al cargar fondo: {e}")
    fondo = pygame.Surface((ANCHO, ALTO))
    fondo.fill((90, 150, 255))
    usando_fondo = False

# configuracion del sprite sheet
FRAME_ANCHO = 64
FRAME_ALTO = 64
COLUMNAS = 4    # Cuatro fotogramas por fila

# escoala para agrandar el personaje
ESCALA = 2.5
ANCHO_ESCALADO = int(FRAME_ANCHO * ESCALA)
ALTO_ESCALADO = int(FRAME_ALTO * ESCALA)

# funcion para extrar los frames
def obtener_frames(fila, num_frames=4):
    """Extrae los frames de una fila del sprite sheet y los escala"""
    frames = []
    for i in range(num_frames):
        rect = pygame.Rect(i * FRAME_ANCHO, fila * FRAME_ALTO, FRAME_ANCHO, FRAME_ALTO)
        frame = sprite_sheet.subsurface(rect)
        # Escalar el frame para hacerlo más grande
        frame_escalado = pygame.transform.scale(frame, (ANCHO_ESCALADO, ALTO_ESCALADO))
        frames.append(frame_escalado)
    return frames

# diccionario de animaciones
animaciones = {
    "arriba": obtener_frames(0),
    "izquierda": obtener_frames(1),
    "abajo": obtener_frames(2),
    "derecha": obtener_frames(3),
    "idle": obtener_frames(4),      # animacion idle
    "ataque": obtener_frames(5)     # animacion ataque
}

# --- Variables de juego ---
x, y = ANCHO // 2 - ANCHO_ESCALADO // 2, ALTO // 2 - ALTO_ESCALADO // 2
velocidad = 4
direccion = "abajo"
estado = "idle"  # Puede ser: "idle", "caminando", "atacando"
frame_index = 0
ultimo_tiempo = pygame.time.get_ticks()
tiempo_animacion = 150  # milisegundos entre cuadros
reloj = pygame.time.Clock()

# Variables de ataque
atacando = False
tiempo_inicio_ataque = 0
duracion_ataque = 400  # milisegundos que dura el ataque

# --- Fuente para texto ---
fuente = pygame.font.Font(None, 28)
fuente_pequena = pygame.font.Font(None, 20)

# --- Bucle principal ---
ejecutando = True
while ejecutando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False
        
        # Detectar ataque con barra espaciadora
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not atacando:
                atacando = True
                estado = "atacando"
                tiempo_inicio_ataque = pygame.time.get_ticks()
                frame_index = 0

    # --- Verificar si el ataque terminó ---
    if atacando:
        tiempo_transcurrido = pygame.time.get_ticks() - tiempo_inicio_ataque
        if tiempo_transcurrido >= duracion_ataque:
            atacando = False
            estado = "idle"

    # --- Movimiento y dirección (solo si NO está atacando) ---
    if not atacando:
        teclas = pygame.key.get_pressed()
        moviendo = False

        if teclas[pygame.K_UP]:
            y -= velocidad
            direccion = "arriba"
            estado = "caminando"
            moviendo = True
        if teclas[pygame.K_DOWN]:
            y += velocidad
            direccion = "abajo"
            estado = "caminando"
            moviendo = True
        if teclas[pygame.K_LEFT]:
            x -= velocidad
            direccion = "izquierda"
            estado = "caminando"
            moviendo = True
        if teclas[pygame.K_RIGHT]:
            x += velocidad
            direccion = "derecha"
            estado = "caminando"
            moviendo = True

        if not moviendo:
            estado = "idle"

    # --- Límites de pantalla ---
    if x < 0:
        x = 0
    elif x + ANCHO_ESCALADO > ANCHO:
        x = ANCHO - ANCHO_ESCALADO
    
    if y < 0:
        y = 0
    elif y + ALTO_ESCALADO > ALTO:
        y = ALTO - ALTO_ESCALADO

    # --- Actualizar animación ---
    ahora = pygame.time.get_ticks()
    
    if estado == "atacando":
        # Animación de ataque
        if ahora - ultimo_tiempo > tiempo_animacion:
            frame_index = (frame_index + 1) % len(animaciones["ataque"])
            ultimo_tiempo = ahora
        animacion_actual = "ataque"
    elif estado == "caminando":
        # Animación de caminar
        if ahora - ultimo_tiempo > tiempo_animacion:
            frame_index = (frame_index + 1) % len(animaciones[direccion])
            ultimo_tiempo = ahora
        animacion_actual = direccion
    else:
        # Animación idle (quieto)
        if ahora - ultimo_tiempo > tiempo_animacion * 2:  # Más lenta
            frame_index = (frame_index + 1) % len(animaciones["idle"])
            ultimo_tiempo = ahora
        animacion_actual = "idle"

    # --- dibujar ---
    # fondo
    VENTANA.blit(fondo, (0, 0))
    
    # personaje
    VENTANA.blit(animaciones[animacion_actual][frame_index], (x, y))
    
    # --- interfaz de usuario ---
    # panel de información
    panel_height = 120
    panel = pygame.Surface((ANCHO, panel_height))
    panel.set_alpha(180)
    panel.fill((20, 20, 40))
    VENTANA.blit(panel, (0, ALTO - panel_height))
    
    # estadistica
    y_info = ALTO - 90
    texto_dir = fuente.render(f"Dirección: {direccion}", True, (200, 255, 200))
    VENTANA.blit(texto_dir, (10, y_info + 25))
    
    texto_pos = fuente.render(f"Posición: ({x}, {y})", True, (255, 200, 150))
    VENTANA.blit(texto_pos, (10, y_info + 50))

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
print("¡Juego cerrado correctamente!")