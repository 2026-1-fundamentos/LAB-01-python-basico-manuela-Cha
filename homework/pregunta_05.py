"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from .leer_archivo import leer_archivo

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """


    datos = {}

    for fila in leer_archivo():
        letra = fila[0]
        numero = int(fila[1])
        if letra not in datos:
            datos[letra] = []
        datos[letra].append(numero)
        
    respuesta = []

    for letra in sorted(datos):
        respuesta.append((letra, max(datos[letra]), min(datos[letra])))

    return respuesta

print(pregunta_05())