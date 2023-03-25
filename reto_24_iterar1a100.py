### Reto #24: ITERATION MASTER ###

"""
Quiero contar del 1 al 100 de uno en uno (imprimiendo cada uno). ¿De cuántas maneras eres capaz de hacerlo? Crea el código para cada una de ellas.
"""

def contarHasta100():
    contador = 0
    for i in range(1,101):
        contador += 1
        print(contador)

contarHasta100()

def contarHasta100_v2():
    x = 0
    while x < 100:
        x += 1
        print(x)

contarHasta100_v2()
