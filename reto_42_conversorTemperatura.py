### Reto #42: CONVERSOR DE TEMPERATURA ###

"""
Enunciado: Crea una función que transforme grados Celsius en Fahrenheit y viceversa.
 * Para que un dato de entrada sea correcto debe poseer un símbolo "°" y su unidad ("C" o "F").
 * En caso contrario retornará un error.
"""

def convertir_temperatura(temp_str):
    if len(temp_str) < 2 or temp_str[-2] != "°":
        raise ValueError("Entrada inválida: se requiere el símbolo '°' y la unidad (C o F)")

    temp = float(temp_str[:-2])
    unit = temp_str[-1]

    if unit == "C":
        return f"{(9/5) * temp + 32}°F"
    elif unit == "F":
        return f"{round((5/9) * (temp - 32), 2)}°C"
    else:
        raise ValueError("Unidad de temperatura inválida. Se requiere 'C' o 'F'.")

print(convertir_temperatura("35°C"))  # 95.0°F
print(convertir_temperatura("100°F")) # 37.78°C
print(convertir_temperatura("35°K")) # Value error