### Reto #8: DECIMAL A BINARIO ###

"""
Crea un programa se encargue de transformar un número decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
"""

def decimal_a_binario(decimal):
    if decimal <= 0:
        return 0
    
    binario = ""
    
    while decimal > 0:
        residuo = int(decimal % 2)
        decimal= int(decimal / 2)
        binario = str(residuo) + binario
    return binario

decimal = int(input('Ingrese un numero decimal: '))
binario = decimal_a_binario(decimal)
print(f"El numero {decimal} en el sistema binario es {binario}")