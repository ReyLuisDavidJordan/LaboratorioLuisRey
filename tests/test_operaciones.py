# tests/test_operaciones.py
import pytest
from src.operaciones import suma, division

def test_suma():
    # Casos normales
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0
    assert suma(0, 0) == 0

def test_division():
    # Casos normales
    assert division(10, 2) == 5.0
    assert division(5, 5) == 1.0
    # Caso borde: división por cero
    assert division(5, 0) == "Error"
