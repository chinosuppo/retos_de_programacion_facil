### Reto #6: INVIRTIENDO CADENAS ###

"""
Crea un programa que invierta el orden de una cadena de texto sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""
frase = str()

def invertir_cadena(frase):
    return frase[::-1]

print(invertir_cadena('Hola mundo'))