### Reto #47: VOCAL MÁS COMÚN ###

"""
Enunciado: Crea un función que reciba un texto y retorne la vocal que más veces se repita.
 * Ten cuidado con algunos casos especiales.
 * Si no hay vocales podrá devolver vacío. 
"""

def vocal_mas_comun(texto):
    # Convertir el texto a minúsculas
    texto = texto.lower()
    # Contar la frecuencia de cada vocal en el texto
    frecuencias = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    for letra in texto:
        if letra in frecuencias:
            frecuencias[letra] += 1
    # Encontrar la vocal con la frecuencia más alta
    vocal_mas_comun = ""
    max_frecuencia = 0
    for vocal, frecuencia in frecuencias.items():
        if frecuencia > max_frecuencia:
            vocal_mas_comun = vocal
            max_frecuencia = frecuencia
    # Si no se encontraron vocales, devolver vacío
    if max_frecuencia == 0:
        return ""
    else:
        return vocal_mas_comun

print(vocal_mas_comun("Racing")) # devuelve a
print(vocal_mas_comun("Boca")) # devuelve a
print(vocal_mas_comun("River")) # devuelve e
print(vocal_mas_comun("Independiente")) # devuelve e
print(vocal_mas_comun("San Lorenzo")) # devuelve o
print(vocal_mas_comun("Unguento")) # devuelve u
print(vocal_mas_comun("DVD")) # no devuelve nada