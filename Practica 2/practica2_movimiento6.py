"""Este codigo mueve un objeto en la pantalla usando las teclas de flecha."""
"""Autor: Jose Juan Padilla B"""
import turtle as t

t.title("Mover con las flechas el cuadrado")

"""Configuracion de la pantalla"""
PANTALLA = t.Screen()
PANTALLA.setup(600, 600)
PANTALLA.bgcolor("lightblue")
LADO = 90 #Parametro global para el lado del cuadrado

def teleport (x:float, y:float): #Segui usando el teleport para dibujar mi figura en cierto punto
    """Aqui movemos el cuadrado a la posicion (x, y)"""
    t.penup()
    t.goto(x, y)
    t.pendown()

def cuadrado (LADO:float):
    """Aqui dibujamos un cuadrado tomando el lado especificado."""
    t.color("black", "yellow")
    t.fillcolor("yellow")
    t.begin_fill()
    for _ in range(4):
        t.forward(LADO)
        t.right(90)
    t.end_fill()
def w():
    """Mover hacia arriba"""
    t.penup()
    t.setheading(90) #Este metodo de la torguga gira la tortuga a un angulo especifico segun la direccion de las agujas del reloj.
    t.fd(50)
    t.clear() # El metodo clear limpia los dibujos hechos por la tortuga.
    cuadrado(LADO)

def s():
    """Mover hacia abajo"""
    t.penup()
    t.setheading(270)
    t.fd(50)
    t.clear()
    cuadrado(LADO)
def a():
    """Mover hacia la izquierda"""
    t.penup()
    t.setheading(180)
    t.fd(50)
    t.clear()
    cuadrado(LADO)
def d():
    """Mover hacia la derecha"""
    t.penup()
    t.setheading(0)
    t.fd(50)
    t.clear()
    cuadrado(90)

def controles_teclas():
    """Aqui definimos los controles del teclado."""
    PANTALLA.listen()
    PANTALLA.onkey(w, "Up") #El metodo onkey recibe una funcion y una tecla en string para definirla como un control, en este caso las flechas.
    PANTALLA.onkey(s, "Down")
    PANTALLA.onkey(a, "Left")
    PANTALLA.onkey(d, "Right")
    
def main():
    """Funcion principal"""
    teleport(-50, 100)
    cuadrado(LADO)
    t.speed(0)
    controles_teclas()
    PANTALLA.mainloop()
    
if __name__ == "__main__":
     main()