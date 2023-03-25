### Reto #22: CONJUNTOS ###

"""
Crea una función que reciba dos array, un booleano y retorne un array.
 * Si el booleano es verdadero buscará y retornará los elementos comunes de los dos array.
 * Si el booleano es falso buscará y retornará los elementos no comunes de los dos array.
 * No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
"""

array_1 = {'Arsenal', 'Manchester City', 'Manchester United', 'Tottenham', 'Liverpool', 'Newcastle', 'Fulham', 'Brighton'}
array_2 = {'Manchester City', 'Liverpool', 'Chelsea', 'Tottenham', 'Arsenal', 'Manchester United', 'West Ham', 'Leicester City'}
bool = True

def equiposComunes(array_1, array_2, bool):
    if (bool == True):
        comunes = array_1.intersection(array_2)
        return comunes
    else:
        noComunes = array_1.symmetric_difference(array_2)
        return noComunes

print(equiposComunes(array_1, array_2, False))
    