# utils.py
# Módulo con funciones básicas de números y texto

# Función sumar: suma dos números enteros
# Entradas: a (int), b (int)
# Salida: int, resultado de a + b
def sumar(a: int, b: int) -> int:
    # Suma de números enteros
    return a + b


# Función contar_vocales: cuenta las vocales de un texto
# Entradas: texto (str)
# Salida: int, número de vocales en el texto
# Errores: lanza TypeError si la entrada no es un string
def contar_vocales(texto: str) -> int:
    # Verifica que el argumento sea un string
    if not isinstance(texto, str):
        raise TypeError("El argumento debe ser un string")
    # Cuenta las vocales en el texto
    return sum(1 for letra in texto.lower() if letra in "aeiou")


# Función es_bisiesto: determina si un año es bisiesto
# Entradas: anio (int)
# Salida: bool, True si es bisiesto, False si no
# Errores: lanza TypeError si la entrada no es un entero
def es_bisiesto(anio: int) -> bool:
    # Verifica que el argumento sea un entero
    if not isinstance(anio, int):
        raise TypeError("El año debe ser un entero")
    # Calcula si el año es bisiesto
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)
