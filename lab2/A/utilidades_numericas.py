# utilidades_numericas.py

def suma_segura(a, b):
    #Suma dos números asegurando que sean válidos (int o float)
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError(f"Ambos argumentos deben ser números: a={a}, b={b}")
    return a + b

def resta_segura(a, b):
    #Resta dos números asegurando que sean válidos (int o float)
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError(f"Ambos argumentos deben ser números: a={a}, b={b}")
    return a - b

def multiplicacion_segura(a, b):
    #Multiplica dos números asegurando que sean válidos (int o float)
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError(f"Ambos argumentos deben ser números: a={a}, b={b}")
    return a * b

def division_segura(a, b):
    #Divide a entre b asegurando que no sea división por cero y que los argumentos sean válidos
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError(f"Ambos argumentos deben ser números: a={a}, b={b}")
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b
