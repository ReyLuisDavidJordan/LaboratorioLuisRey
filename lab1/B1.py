def parsear_enteros(entradas: list[str]) -> tuple[list[int], list[str]]:
    valores = []
    errores = []

    for i, elemento in enumerate(entradas):
        try:
            numero = int(elemento)
            valores.append(numero)
        except ValueError:
            errores.append(f"Error: '{elemento}' en la posición {i} no es un entero válido.")

    return valores, errores

# Entrada interactiva del usuario
entrada_usuario = input("Ingresa números separados por comas: ")
entradas = [x.strip() for x in entrada_usuario.split(",")]

valores, errores = parsear_enteros(entradas)

print("\nValores convertidos:", valores)
print("Errores encontrados:", errores)
