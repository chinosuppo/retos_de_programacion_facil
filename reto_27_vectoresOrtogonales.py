### Reto #27: VECTORES ORTOGONALES ###

"""
Crea un programa que determine si dos vectores son ortogonales.
 * Los dos array deben tener la misma longitud.
 * Cada vector se podría representar como un array. Ejemplo: [1, -2]
"""

def vectoresOrtogonales(vector_1, vector_2):
    lenght_1 = len(vector_1)
    lenght_2 = len(vector_2)
    if lenght_1 == lenght_2:
        escalar = (vector_1[0]*vector_2[0]) + (vector_1[1]*vector_2[1])
        if (escalar == 0):
            return True
        else:
            return False
    else:
        return "Ingrese dos vectores con la misma longitud"

print(vectoresOrtogonales(vector_1=[3,2], vector_2=[-2,3])) # True
print(vectoresOrtogonales(vector_1=[3,1], vector_2=[-2,3])) # False
print(vectoresOrtogonales(vector_1=[3,2], vector_2=[-2,3,5])) # "Ingrese dos vectores con la misma longitud"