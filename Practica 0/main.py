""" Practica 0 Explorando la tortuga"""
import turtle as t
from random import random

def teleport(x : float, y : float) -> None:
    """Esta funcion es para trasladar el punto de inicio sin afectar alguna otra figura en la grafica"""
    t.penup()
    t.setx(x)
    t.sety(y)
    t.pendown()
    
def dibuja():
    """Esta funcion dibuja un cuadrado"""
    for _ in range(100):
        steps = int(random() * 100)
        angle = int(random() * 100)
        t.right(angle)
        t.fd(steps)
        
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
teleport(300,300)
t.circle(20)
input("El circulo es :")

