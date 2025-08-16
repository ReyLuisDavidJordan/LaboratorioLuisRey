class CantidadInvalida(Exception):
    pass
def calcular_total(precio_unitario, cantidad):
    if cantidad <= 0:
        raise CantidadInvalida(f"La cantidad ingresada ({cantidad}) no es válida. Debe ser mayor a 0")
    if precio_unitario < 0:
        raise ValueError(f"El precio unitario ({precio_unitario}) no puede ser negativo")
    return precio_unitario * cantidad

# Interfaz interactiva
try:
    precio_input = float(input("Ingresa el precio unitario:"))
    cantidad_input = int(input("Ingresa la cantidad:"))
    
    total = calcular_total(precio_input, cantidad_input)
    print(f"Total: {total:.2f}")

except CantidadInvalida as ci:
    print(f"Error de cantidad: {ci}")
except ValueError as ve:
    print(f"Error de valor: {ve}")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
