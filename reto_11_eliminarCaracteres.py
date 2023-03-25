### Reto #11: ELIMINANDO CARACTERES ###

"""
Crea una función que reciba dos cadenas como parámetro (str1, str2) e imprima otras dos cadenas como salida (out1, out2).
 * out1 contendrá todos los caracteres presentes en la str1 pero NO estén presentes en str2.
 * out2 contendrá todos los caracteres presentes en la str2 pero NO estén presentes en str1.
"""

def caracteres_diferentes(str1, str2):
    out1 = ''.join(letra for letra in str1.lower() if letra not in str2.lower())
    out2 = ''.join(letra for letra in str2.lower() if letra not in str1.lower())
    print(f"out1: {out1}\nout2: {out2}")

caracteres_diferentes('Hola', 'hola') # No devuelve nada
caracteres_diferentes('Hola', 'Mama') # out1 = hol, out2 = mm