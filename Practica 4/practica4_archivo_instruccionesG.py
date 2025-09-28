"""Practica 4 Lector de instrucciones para turtle
   Autor: Jose Juan Padilla"""
import turtle

# Variables globales
t = None
pantalla = None

def inicializar_turtle():
    """Configura turtle de manera sencilla"""
    global t, pantalla
    pantalla = turtle.Screen()
    pantalla.setup(600, 600)
    pantalla.title("Practica 4 - Dibujante Interactivo")
    pantalla.bgcolor("white")
    
    t = turtle.Turtle()
    t.speed(3)
    return t

def teleport(x, y): #funciones ya utilizadas anteriormente
    """Mueve la tortuga sin dejar rastro"""
    t.penup()
    t.goto(x, y)
    t.pendown()

def cuadrado(lado):
    """Dibuja un cuadrado con relleno"""
    for _ in range(4):
        t.forward(lado)
        t.right(90)


def triangulo(lado):
    """Dibuja un triangulo con relleno"""
    for _ in range(3):
        t.forward(lado)
        t.right(120)

def circulo(radio):
    """Dibuja un circulo con relleno"""
    t.circle(radio)

def linea(longitud):
    """Dibuja una linea gruesa"""
    t.pensize(5)
    t.forward(longitud)
    t.pensize(1)

def ejecutar_comando(linea):
    """Ejecuta un comando"""
    partes = linea.strip().split() # Divide la linea en partes
    if not partes: # Ignora lineas vacias
        return True
    
    comando = partes[0].lower() # Convertir a minusculas para evitar errores
    
    try: # Manejo de errores basico
        if comando == "cuadrado" and len(partes) == 2: # Verifica que el comando y numero de argumentos sean correctos
            cuadrado(int(partes[1]))
            return True
        
        elif comando == "triangulo" and len(partes) == 2:
            triangulo(int(partes[1]))
            return True
        
        elif comando == "circulo" and len(partes) == 2:
            circulo(int(partes[1]))
            return True
        
        elif comando == "linea" and len(partes) == 2:
            linea(int(partes[1]))
            return True
        
        elif comando == "teleport" and len(partes) == 3:
            teleport(int(partes[1]), int(partes[2]))
            return True
        
        elif comando == "avanzar" and len(partes) == 2:
            t.forward(int(partes[1]))
            return True
        
        elif comando == "girar" and len(partes) == 2:
            t.right(int(partes[1]))
            return True
        
        elif comando == "color" and len(partes) == 2:
            t.color(partes[1])
            return True
        
        elif comando == "casa":
            t.home()
            return True
        
        elif comando == "limpiar":
            t.clear()
            return True
        
        elif comando == "salir":
            return "salir"
        
        else: # Comando no reconocido
            print(f"⚠ Comando no reconocido: {linea}") # Mensaje de advertencia
            return False
    
    except Exception as e:# Captura cualquier error en la ejecucion del comando como se vio en la documentacion
        print(f"⚠ Error ejecutando '{linea}': {e}")
        return False

def modo_interactivo(): #funcion para interactuar con el usuario
    """Permite escribir comandos en tiempo real"""
    print("\n=== MODO INTERACTIVO CON EL USUARIO ===")
    print("Escribe comandos (o 'salir' para terminar):")
    print("Ejemplo: cuadrado 50")
    print()
    
    while True: # Bucle infinito hasta que el usuario decida salir
        try:
            comando = input("Comando > ") # Solicita comando al usuario
            
            if not comando.strip(): # Ignora lineas vacias
                continue
                
            resultado = ejecutar_comando(comando) # Ejecuta el comando y guarda el resultado
            
            if resultado == "salir":
                print("¡Adiós!")
                break
            elif resultado:
                print("  ✓ Comando ejecutado")
            else:
                print("  ❌ Comando invalido")
                
            pantalla.update()
            
        except KeyboardInterrupt: # Manejo de Ctrl+C para salir
            print("\n¡Bye Bye!")
            break

def leer_archivo():
    """Lee y ejecuta las instrucciones del archivo"""
    try:
        with open("dibujante.txt", "r") as archivo: # Abre el archivo en modo lectura
            lineas = archivo.readlines() # Lee todas las lineas del archivo
        
        print("=== EJECUTANDO ARCHIVO ===")
        comandos_ok = 0 # Contadores de comandos exitosos y con error
        comandos_error = 0
        
        for i, linea in enumerate(lineas, 1): # Itera sobre las lineas con su numero
            linea = linea.strip() # Elimina espacios en blanco
            
            if not linea or linea.startswith("#"): # Ignora lineas vacias o comentarios
                continue
            
            print(f"Línea {i}: {linea}") # Muestra la linea actual
            
            if ejecutar_comando(linea): # Ejecuta el comando y verifica si fue exitoso
                print("  ✓ OK")
                comandos_ok += 1
            else: # Si hubo error
                print("  ❌ ERROR")
                comandos_error += 1
            
            pantalla.update() # Actualiza la pantalla para mostrar el dibujo
        
        print(f"\nArchivo ejecutado: {comandos_ok} OK, {comandos_error} errores") 
        return True
        
    except FileNotFoundError: # Manejo de error si el archivo no existe
        print("❌ No se encontro 'dibujante.txt'")
        return False

def mostrar_ayuda(): #funcion para mostrar los comandos disponibles al usuario
    """Muestra los comandos disponibles"""
    print("=== COMANDOS DISPONIBLES ===")
    print("cuadrado 50      - Dibuja cuadrado rojo de 50px")
    print("triangulo 60     - Dibuja triángulo azul de 60px") 
    print("circulo 30       - Dibuja círculo morado de 30px")
    print("linea 80         - Dibuja línea naranja de 80px")
    print("teleport -100 50 - Mueve sin rastro a (-100, 50)")
    print("avanzar 50       - Avanza 50 píxeles")
    print("color red        - Cambia color (red, blue, green, etc)")
    print("casa             - Regresa al centro (0,0)")
    print("limpiar          - Borra todo el dibujo")
    print("salir            - Termina el programa")
    print()

def main():
    """Funcion principal con menu"""
    print("=== PRÁCTICA 4 - ===")
    
    inicializar_turtle()
    mostrar_ayuda()
    
    while True: # Bucle principal del menu
        print("¿Que te gustaria hacer hacer?")
        print("1. Ejecutar archivo 'dibujante.txt'")
        print("2. Escribir comandos interactivamente")
        print("3. Mostrar ayuda")
        print("4. Salir")
        
        opcion = input("\nElige opción (1-4): ").strip() # Solicita opcion al usuario
        
        if opcion == "1":
            leer_archivo()
        
        elif opcion == "2":
            modo_interactivo()
        
        elif opcion == "3":
            mostrar_ayuda()
        
        elif opcion == "4":
            print("¡Hasta luego!")
            pantalla.bye()
            break
        
        else:
            print("❌ Opción inválida. Usa 1, 2, 3 o 4") # Manejo de opcion invalida

if __name__ == "_main_":
    main()