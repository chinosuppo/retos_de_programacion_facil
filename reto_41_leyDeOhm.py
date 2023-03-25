### Reto #41: LA LEY DE OHM ###

"""
Enunciado: Crea una función que calcule el valor del parámetro perdido correspondiente a la ley de Ohm.
 * Enviaremos a la función 2 de los 3 parámetros (V, R, I), y retornará el valor del tercero (redondeado a 2 decimales).
 * Si los parámetros son incorrectos o insuficientes, la función retornará la cadena de texto "Invalid values".
"""

def calcular_ley_ohm(voltaje, intensidad, resistencia):
    if voltaje is None:
        return round(intensidad * resistencia, 2)
    elif intensidad is None:
        return round(voltaje / resistencia, 2)
    elif resistencia is None:
        return round(voltaje / intensidad, 2)
    else:
        return ValueError("Debe proporcionar exactamente dos parámetros.")

print(calcular_ley_ohm(8, 4, None)) # 2.0
print(calcular_ley_ohm(None, 4, 3)) # 12
print(calcular_ley_ohm(8, None, 10)) # 0.8