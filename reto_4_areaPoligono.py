### Reto #4: ÁREA DE UN POLÍGONO ###

"""
Crea una única función (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
 * La función recibirá por parámetro sólo UN polígono a la vez.
 * Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * Imprime el cálculo del área de un polígono de cada tipo.
"""

def calcular_area_poligono(opcion):
    if (opcion == 1):
        base_triangulo = int(input("Ingrese el valor de la base del triangulo: "))
        altura_triangulo = int(input("Ingrese el valor de la altura del triangulo: "))
        area_triangulo = (base_triangulo * altura_triangulo) / 2
        print(altura_triangulo)
    elif (opcion == 2):
        lado_cuadrado = int(input("Ingrese el valor de los lados del cuadrado: "))
        area_cuadrado = lado_cuadrado ** 2
        print(area_cuadrado)
    elif (opcion == 3):
        base_rectangulo = int(input("Ingrese el valor de la base del rectangulo: "))
        altura_rectangulo = int(input("Ingrese el valor de la altura del rectangulo: "))
        area_rectangulo = (base_rectangulo * altura_rectangulo)
        print(area_rectangulo)
    else:
        print("OPCIÓN INCORRECTA")
        
calcular_area_poligono(opcion = int(input("Elige que area quieres calcular\n1)Triangulo\n2)Cuadrado\n3)Rectangulo\n")))