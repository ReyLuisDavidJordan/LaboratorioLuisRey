# Definición de funciones
def saludar(nombre):
    return f"Hola {nombre}"

def despedir(nombre):
    return f"Adiós {nombre}"

def aplaudir(nombre):
    return f" *aplausos* {nombre} "

# Diccionario que mapea el nombre de la acción a la función
acciones = {
    "saludar": saludar,
    "despedir": despedir,
    "aplaudir": aplaudir
}

# Función para ejecutar acciones
def ejecutar(accion, *args, **kwargs):
    if accion not in acciones:
        raise ValueError(f"Acción '{accion}' no encontrada. Acciones disponibles: {list(acciones.keys())}")
    return acciones[accion](*args, **kwargs)

# Menú interactivo
while True:
    print("\n MENÚ DE ACCIONES")
    print("1. Saludar")
    print("2. Despedir")
    print("3. Aplaudir")
    print("4. Salir")

    opcion = input("Elige una opción (1-4) ")

    if opcion == "4":
        print("Saliendo del programa")
        break

    # Mapeo de opciones a acciones
    opcion_accion = {
        "1": "saludar",
        "2": "despedir",
        "3": "aplaudir"
    }

    try:
        accion = opcion_accion[opcion]  # Si no existe, salta KeyError
    except KeyError:
        print(f"Opción inválida. Debe ser {list(opcion_accion.keys())} o 4 para salir.")
        continue  # Volver al menú

    #Si el try transcurre sin errores seguimos aqui
    nombre = input("Introduce el nombre: ")

    try:
        print(ejecutar(accion, nombre))
    except ValueError as e:
        print(f"Error: {e}")

