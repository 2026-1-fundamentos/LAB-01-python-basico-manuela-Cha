"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

from .leer_archivo import leer_archivo
def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    datos = {}

    for fila in leer_archivo():
        letra = fila[0]
        if letra not in datos:
            datos[letra] = 0
        for elemento in fila[4].split(","):
            valor = int(elemento.split(":")[1])
            datos[letra] += valor

    return dict(sorted(datos.items()))

print(pregunta_12())