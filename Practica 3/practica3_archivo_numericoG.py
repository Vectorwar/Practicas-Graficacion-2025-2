"""Practica 3: Archivo numerico en txt y dibujo con turtle"""
"""Autor: Jose Juan Padilla"""
import turtle
import random

# Diccionario para los colores
COLORES_NUMERADOS = {
    0: "black", 1: "red", 2: "blue", 3: "green", 4: "yellow",
    5: "purple", 6: "orange", 7: "pink", 8: "cyan", 9: "brown"
}

def crear_archivo():
    """Creamos el archivo con la matriz 100x100"""
    print("Creando archivo matriz_100x100.txt...")
   
    with open("matriz_100x100.txt", "w") as archivo:
        for fila in range(100):
            linea = []
            for columna in range(100):
                numero = random.randint(0, 9)  # Agrega numeros aleatorios del 0-9
                linea.append(str(numero))  # convertir a string para escribir en el archivo
            archivo.write(" ".join(linea) + "\n")  # Escribir la linea del archivo
   
    print("¡Archivo creado!")  # Mensaje para el usuario

def cargar_matriz():
    """Carga los numeros del archivo"""
    print("Cargando matriz...")
    matriz = []
   
    with open("matriz_100x100.txt", "r") as archivo:
        for linea in archivo:
            fila = []
            numeros = linea.split()
            for num in numeros:
                fila.append(int(num)) # Convertir a entero
            matriz.append(fila) # Agregar fila a la matriz
   
    return matriz

def seleccionar_color(numero): 
    """Devuelve el color según el numero usando el diccionario"""
    return COLORES_NUMERADOS[numero]

def dibujar_matriz(matriz):
    """Dibuja la matriz con turtle"""
    # Configuramos turtle
    screen = turtle.Screen()
    screen.setup(600, 800)
    screen.bgcolor("white")
    screen.title("Práctica 3")
   
    t = turtle.Turtle()
    t.speed(0)
    t.penup() # No dibujar líneas
    t.shape("square") # Usar forma cuadrada para pixeles
    t.shapesize(0.05, 0.05) # Tamaño del pixel
   
    # Empezar desde arriba a la izquierda
    inicio_x = -250
    inicio_y = 250
   
    for fila in range(100):# Recorrer cada fila
        
        for columna in range(100): # Recorrer cada columna
            # Obtener número y color para la matriz
            numero = matriz[fila][columna]
            color = seleccionar_color(numero)
           
            # Calcular posición
            x = inicio_x + columna * 5 # Espacio entre pixeles
            y = inicio_y - fila * 5
           
            # Dibujar píxel
            t.goto(x, y)
            t.color(color)
            t.stamp() # Dibujar el pixel como un sello
   
    print("¡Terminado! Haz clic para cerrar.")
    screen.exitonclick()

def main():
    """Programa principal"""
    print("=== PRACTICA 3 ===")
   
    # 1. Crear archivo
    crear_archivo()
   
    # 2. Cargar matriz
    matriz = cargar_matriz()
    
    # 4. Dibujar con turtle
    print("\nPresiona Enter para comenzar a dibujar...")
    input()
    dibujar_matriz(matriz)

if __name__ == "__main__":
    main()