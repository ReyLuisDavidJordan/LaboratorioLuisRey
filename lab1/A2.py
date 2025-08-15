def crear_descuento(porcentaje):
    def aplicar_descuento(precio):
        return precio * (1 - porcentaje)
    return aplicar_descuento

# Crear funciones de descuento reutilizables
descuento10 = crear_descuento(0.10)
descuento25 = crear_descuento(0.25)

# Interfaz interactiva
while True:
    print("\nCalcular descuento")
    print("1. Aplicar 10% de descuento")
    print("2. Aplicar 25% de descuento")
    print("3. Salir")
    
    opcion = input("Elige una opción 1-3 ")
    
    if opcion == "1":
        precio = float(input("Ingresa el precio: "))
        print(f"Precio final: {descuento10(precio):.2f}")
    elif opcion == "2":
        precio = float(input("Ingresa el precio: "))
        print(f"Precio final: {descuento25(precio):.2f}")
    elif opcion == "3":
        print("Cerrando programa")
        break
    else:
        print("Opcion no valida")
