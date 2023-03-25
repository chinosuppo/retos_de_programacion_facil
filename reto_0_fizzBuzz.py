### Reto #0: EL FAMOSO "FIZZ BUZZ” ###

"""
Escribe un programa que muestre por consola (con un print) los números de 1 a 100 (ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:
 * Múltiplos de 3 por la palabra "fizz".
 * Múltiplos de 5 por la palabra "buzz".
 * Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

numeros = range(1, 101)

for numero in numeros:
    if numero % 3 == 0 and numero % 5 == 0:
        print(numero,"FIZZBUZZ\n")
    elif numero % 5 == 0:
        print(numero,"BUZZ\n")
    elif numero % 3 == 0:
        print(numero,"FIZZ\n")
    else:
        print(numero, "No es multiplo ni de 3 ni de 5\n")