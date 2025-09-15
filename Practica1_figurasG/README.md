Practica figuras.

Esta practica se realizo con la version de python 3.10.11.

 # Profe aqui quise poner este codigo en vez de t.circle(), pero es mas lento, hace los mismo pero es malento, camina uno y se para la derecha hasta llegar a los 360 pasos

def circulo() -> None:
    """Dibuja un circulo."""  
    t.color("green", "purple")
    t.begin_fill()
    for _ in range(360):
        t.forward(1)
        t.right(1)
    t.end_fill()
