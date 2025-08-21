import sys, os
sys.path.insert(0, os.path.abspath("../src"))

from lab5.src.csv_utils import leer_csv, validar_columnas, validar_tipos

import pytest

# Ruta al CSV de ejemplo
CSV_PATH = "tests/iris.csv"  

# Columnas obligatorias que deben existir en el CSV
COLUMNAS = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]

# Tipos esperados para validar cada columna
TIPOS = {
    "sepal_length": float,
    "sepal_width": float,
    "petal_length": float,
    "petal_width": float
}

# Test para verificar que el CSV se puede leer y no esté vacío
def test_leer_csv():
    filas = leer_csv(CSV_PATH)
    assert len(filas) > 0  # debe tener al menos una fila

# Test para verificar que existan todas las columnas obligatorias
def test_columnas():
    filas = leer_csv(CSV_PATH)
    assert validar_columnas(filas, COLUMNAS) is True

# Test para verificar que los tipos de datos sean correctos
def test_tipos():
    filas = leer_csv(CSV_PATH)
    assert validar_tipos(filas, TIPOS) is True

# Test para asegurar que valores numéricos no sean negativos
def test_no_negativos():
    filas = leer_csv(CSV_PATH)
    for fila in filas:
        for col in TIPOS.keys():
            assert float(fila[col]) >= 0  # todos los valores deben ser >= 0

# Test opcional para verificar IDs únicos si existiera una columna 'id'
def test_ids_unicos():
    filas = leer_csv(CSV_PATH)
    if 'id' in filas[0]:  # solo si la columna 'id' existe
        ids = [fila['id'] for fila in filas]
        assert len(ids) == len(set(ids))  # todos los IDs deben ser únicos
