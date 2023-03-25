### Reto #13: FACTORIAL RECURSIVO ###

"""
Escribe una función que calcule y retorne el factorial de un número dado de forma recursiva.
"""

def factorial(n):
    fact = 1
    for num in range(2, n + 1): # Recordar que en el rango el valor despues de la coma no lo toma
        fact *= num
    return fact

print(factorial(3))