"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from .leer_archivo import leer_archivo

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """

    suma = {}

    for fila in leer_archivo():
        letra = fila[0]
        numero = int(fila[1])
        if letra not in suma:
            suma[letra] = 0
        suma[letra] += numero

    return sorted(suma.items())

print(pregunta_03()) 