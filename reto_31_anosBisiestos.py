### Reto #31: AÑOS BISIESTOS ###

"""
Crea una función que imprima los 30 próximos años bisiestos siguientes a uno dado.
 * Utiliza el menor número de líneas para resolver el ejercicio.
"""

def anioBisiesto(anio):
    if (anio % 4 == 0) or (anio % 400 == 0):
        return True
    else:
        return False
    
print(anioBisiesto(2002)) # False
print(anioBisiesto(2020)) # True

anioBisiesto_v2 = lambda anio: True if (anio % 4 == 0) or (anio % 400 == 0) else False

print(anioBisiesto_v2(2004)) # True
print(anioBisiesto_v2(2007)) # False