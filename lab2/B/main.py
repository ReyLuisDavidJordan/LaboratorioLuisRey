# main.py
import mi_paquete.operaciones as op
import mi_paquete.validaciones as val

def pedir_numero(mensaje, tipo=float):
   
    while True:
        try:
            valor = tipo(input(mensaje))
            return valor
        except ValueError:
            print("Entrada inválida. Por favor ingresa un número válido.")

def pedir_operacion():
    print("\n--- Operaciones del paquete ---")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. Validar número positivo")
    while True:
        opcion = input("Elige una opción (1-4): ")
        if opcion in ["1", "2", "3", "4"]:
            return opcion
        else:
            print("Opción inválida. Intenta de nuevo.")

# Interfaz interactiva
while True:
    operacion = pedir_operacion()
    
    if operacion in ["1", "2", "3"]:
        a = pedir_numero("Ingresa el primer número: ")
        b = pedir_numero("Ingresa el segundo número: ")

    try:
        if operacion == "1":
            resultado = op.suma(a, b)
            print(f"Resultado de la suma: {resultado}")
        elif operacion == "2":
            resultado = op.resta(a, b)
            print(f"Resultado de la resta: {resultado}")
        elif operacion == "3":
            resultado = op.multiplicacion(a, b)
            print(f"Resultado de la multiplicación: {resultado}")
        elif operacion == "4":
            numero = pedir_numero("Ingresa el número a validar positivo: ")
            val.requiere_positivo(numero)
            print(f"✅ El número {numero} es positivo.")

       
        continuar = input("\n¿Deseas realizar otra operación? (s/n): ").strip().lower()
        if continuar != "s":
            print("Salir")
            break

    except ValueError as ve:
        print(f"Error de validación: {ve}")
