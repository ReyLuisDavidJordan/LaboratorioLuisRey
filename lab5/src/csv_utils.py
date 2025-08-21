# csv_utils.py
# Módulo para leer y validar archivos CSV con columnas y tipos normalizados

import csv

# Diccionario de mapeo entre nombres de columnas del CSV y los nombres esperados por los tests
# Ejemplo: "sepal.length" en el CSV se convierte en "sepal_length"
COLUMNAS_MAP = {
    "sepal.length": "sepal_length",
    "sepal.width": "sepal_width",
    "petal.length": "petal_length",
    "petal.width": "petal_width",
    "variety": "species"
}


# Función leer_csv

# Lee un archivo CSV y devuelve una lista de diccionarios con nombres de columnas normalizados
# Entrada:
#   ruta (str): ruta al archivo CSV
# Salida:
#   list[dict]: lista de filas con columnas normalizadas
def leer_csv(ruta):
    # Abrir el CSV con utf-8
    with open(ruta, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        filas = []
        for row in lector:
            # Renombrar columnas usando el mapeo si existe,
            # si no existe, reemplazar '.' por '_'
            row_normalizado = {COLUMNAS_MAP.get(k, k.replace(".", "_")): v for k, v in row.items()}
            filas.append(row_normalizado)
        return filas


# Función validar_columnas

# Valida que todas las columnas obligatorias estén presentes en el CSV
# Entrada:
#   filas (list[dict]): lista de diccionarios del CSV
#   columnas_obligatorias (list[str]): lista de columnas que deben existir
# Salida:
#   True si todas las columnas obligatorias están presentes
# Errores:
#   ValueError si el CSV está vacío o falta alguna columna obligatoria
def validar_columnas(filas, columnas_obligatorias):
    if not filas:
        raise ValueError("CSV vacío")
    for col in columnas_obligatorias:
        if col not in filas[0]:
            raise ValueError(f"Columna obligatoria '{col}' no encontrada")
    return True


# Función validar_tipos

# Valida que los valores de cada columna coincidan con el tipo esperado
# Entrada:
#   filas (list[dict]): lista de diccionarios del CSV
#   tipos_esperados (dict[str, type]): diccionario que indica el tipo esperado de cada columna
# Salida:
#   True si todos los valores cumplen con los tipos esperados
# Errores:
#   TypeError si algún valor no coincide con el tipo esperado
def validar_tipos(filas, tipos_esperados):
    for i, fila in enumerate(filas, start=1):
        for col, tipo in tipos_esperados.items():
            try:
                # Intentar convertir el valor al tipo esperado
                tipo(fila[col])
            except ValueError:
                raise TypeError(f"Fila {i}, columna '{col}' no coincide con el tipo {tipo.__name__}")
    return True


# Ejemplo de uso

if __name__ == "__main__":
    # Ruta del archivo CSV
    ruta_csv = "iris.csv"

    # Columnas obligatorias que deben existir en el CSV
    columnas_obligatorias = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]

    # Tipos esperados para cada columna
    tipos_esperados = {
        "sepal_length": float,
        "sepal_width": float,
        "petal_length": float,
        "petal_width": float,
        "species": str
    }

    # Leer CSV
    filas = leer_csv(ruta_csv)

    # Validar que todas las columnas obligatorias existan
    validar_columnas(filas, columnas_obligatorias)

    # Validar que los valores tengan los tipos correctos
    validar_tipos(filas, tipos_esperados)

    # Confirmación de que todo está correcto
    print("CSV leído y validado correctamente")
