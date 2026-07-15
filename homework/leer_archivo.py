
import os
script_dir = os.path.dirname(__file__)
data_path = os.path.abspath(os.path.join(script_dir, '..', 'files', 'input', 'data.csv'))

def leer_archivo():
    with open(data_path, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            yield linea.strip().split("\t")