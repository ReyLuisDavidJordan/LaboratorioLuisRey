# Función para validar que todos los números sean positivos
def requiere_positivos(*args):
    for i, valor in enumerate(args):
        if not isinstance(valor, (int, float)):
            raise TypeError(f"El argumento en la posición {i} ({valor}) no es un número")
        if valor <= 0:
            raise ValueError(f"El argumento en la posición {i} ({valor}) debe ser mayor a 0")

# Función calcular descuento
def calcular_descuento(precio, porcentaje):
    requiere_positivos(precio, porcentaje)
    return precio * (1 - porcentaje)

# Función escalar 
def escala(valor, factor):
    requiere_positivos(valor, factor)
    return valor * factor

# Interfaz interactiva
print("C1")
print("1. Calcular descuento")
print("2. Escalar numero")

opcion = input("Elige una opcion (1-2): ")

try:
    if opcion == "1":
        precio = float(input("Ingresa el precio: "))
        porcentaje = float(input("Ingresa el porcentaje de descuento (ejemplo 0.1 = 10%)"))
        total = calcular_descuento(precio, porcentaje)
        print(f"Precio con descuento: {total:.2f}")

    elif opcion == "2":
        valor = float(input("Ingresa el valor: "))
        factor = float(input("Ingresa el factor de escala: "))
        resultado = escala(valor, factor)
        print(f"Valor escalado: {resultado:.2f}")

    else:
        print("Opción inválida.")

except ValueError as ve:
    print(f"Error de valor: {ve}")
except TypeError as te:
    print(f"Error de tipo: {te}")
