"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv
import os

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.
    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]
    """

    script_dir = os.path.dirname(__file__)
    data_path = os.path.abspath(os.path.join(script_dir, '..', 'files', 'input', 'data.csv'))

    counts = {}
    with open(data_path, encoding='utf-8', newline='') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            if row:
                letter = row[0]
                counts[letter] = counts.get(letter, 0) + 1

    result = sorted(counts.items())
    return result

#print(pregunta_02())
     
