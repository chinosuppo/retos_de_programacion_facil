### Reto #32: EL SEGUNDO ###

"""
Dado un listado de números, encuentra el SEGUNDO más grande.
"""

list_numeros = [4, 6, 79, 66, 98, 1, 2, 43, 56, 99]

def encontrar_segundo_mayor():
    list_numeros.sort(reverse=True)
    segundo = list_numeros[1]
    print(segundo)

encontrar_segundo_mayor()
        