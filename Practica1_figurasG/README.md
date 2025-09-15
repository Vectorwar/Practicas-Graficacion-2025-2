# En esta practica crearemos 4 figuras con ayuda del modulo turtle, asi mismo les daremos color y posicion.
Mediante la documentacion de turtle con python, iremos agregando segun la lectura nuevas funciones que vienen en este modulo.

Esta practica se realizo con la version de python 3.10.11.

 Profe aqui quise poner este codigo en vez de t.circle(), 
 pero es mas lento, hace los mismo pero es malento, camina uno 
 y se para la derecha hasta llegar a los 360 pasos

def circulo() -> None:
    """Dibuja un circulo."""  
    t.color("green", "purple")
    t.begin_fill()
    for _ in range(360):
        t.forward(1)
        t.right(1)
    t.end_fill()
