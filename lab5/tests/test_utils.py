# test_utils.py
# Pruebas unitarias para el módulo utils.py usando pytest
# Se agregan rutas al sys.path para importar utils desde ../src
import sys, os
sys.path.insert(0, os.path.abspath("../src"))

# Importar funciones a probar
from lab5.src.utils import sumar, contar_vocales, es_bisiesto

import pytest


# Tests para la función sumar

# Verifica resultados correctos para números válidos
def test_sumar():
    assert sumar(2, 3) == 5         # Caso normal
    assert sumar(-1, 1) == 0        # Suma con negativo
    assert sumar(0, 0) == 0         # Caso límite con ceros


# Tests para la función contar_vocales

# Verifica resultados correctos para textos válidos
def test_contar_vocales():
    assert contar_vocales("hola") == 2       # Texto con 2 vocales
    assert contar_vocales("xyz") == 0        # Texto sin vocales
    assert contar_vocales("") == 0           # Texto vacío (caso límite)

    # Verifica que se lance error al pasar un tipo inválido
    with pytest.raises(TypeError):
        contar_vocales(123)

# Tests para la función es_bisiesto

# Verifica resultados correctos para años válidos
def test_es_bisiesto():
    assert es_bisiesto(2020) is True   # Divisible por 4, no por 100
    assert es_bisiesto(1900) is False  # Divisible por 100, no por 400
    assert es_bisiesto(2000) is True   # Divisible por 400

    # Verifica que se lance error al pasar un tipo inválido
    with pytest.raises(TypeError):
        es_bisiesto("2020")
