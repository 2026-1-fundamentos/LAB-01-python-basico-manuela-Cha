"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

from .leer_archivo import leer_archivo

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """


    datos = {}

    for fila in leer_archivo():
        elementos = fila[4].split(",")
        for elemento in elementos:
            clave, valor = elemento.split(":")
            valor = int(valor)
            if clave not in datos:
                datos[clave] = []
            datos[clave].append(valor)

    respuesta = []

    for clave in sorted(datos):
        respuesta.append((clave, min(datos[clave]), max(datos[clave])))

    return respuesta

print (pregunta_06())   
