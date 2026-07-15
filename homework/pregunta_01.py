"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
import os

def pregunta_01():
    """
    Retorne la suma de la segunda columna.
    Rta/
    214
    """

    script_dir = os.path.dirname(__file__)
    data_path = os.path.abspath(os.path.join(script_dir, '..', 'files', 'input', 'data.csv'))

    suma = 0
    with open(data_path, encoding='utf-8', newline='') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            if row:
                suma += int(row[1])
    return suma

#print(pregunta_01())