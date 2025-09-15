"""En esta practia vamos a generar figuras con turtle."""
# pylint: disable=no-member
import turtle
t = turtle.Turtle()

# Configuracion inicial
PANTALLA = turtle.Screen()
t.speed(5) # Velocidad de dibujo

def teleport(x: float, y: float) -> None:
    """Mueve la tortuga a la posicion (x, y) sin dejar rastro."""
    t.penup()
    t.goto(x, y)
    t.pendown()

def cuadrado(lado : float) -> None:
    """Dibuja un cuadrado de lado 'lado'."""
    t.color("black", "red") # Color del borde y del relleno
    t.begin_fill() # Inicia el relleno
    for _ in range(4):
        t.forward(lado)
        t.right(90)
    t.end_fill() # Termina el relleno

def triangulo(lado : float) -> None:
    """Aqui dibujaremos un triangulo equilatero de lado a lado."""
    t.color("yellow", "blue")
    t.begin_fill()
    for _ in range(3):
        t.forward(lado)
        t.right(120)
    t.end_fill()

def circulo(radio : float) -> None:
    """Dibuja un circulo."""
    t.color("green", "purple")
    t.begin_fill()
    t.circle(radio)
    t.end_fill()

def linearecta(longitud : float) -> None:
    """Dibuja una linea recta de longitud."""
    t.color("green", "orange")
    t.begin_fill()
    t.pensize(10) # Grosor de la linea
    t.forward(longitud)
    t.pensize(1) # Restaurar grosor
    t.end_fill()

def main():
    """Funcion principal para ejecutar todas las figuras"""
    # Parametros para el cuadrado
    lado = 90
    teleport(-400, 200)
    cuadrado(lado)
    # Parametros para el triangulo
    lado = 90
    teleport(-240, 190)
    triangulo(lado)
    # Parametros para el circulo
    radio = 45
    teleport(-60, 105)
    circulo(radio)
    #Parametros de la linea recta
    longitud = 90
    teleport(60, 150)
    linearecta(longitud)
    PANTALLA.mainloop()  # Mantiene la ventana abierta
if __name__ == "__main__":
    main()