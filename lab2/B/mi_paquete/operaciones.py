

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b


from .validaciones import requiere_positivo

def multiplicacion(a, b):
    requiere_positivo(a, b)
    return a * b
