# main.py
import utilidades_numericas as un

def pedir_numero(mensaje, tipo=float):
    #Pide al usuario un número y valida que sea del tipo correcto, repitiendo hasta que ingrese un valor válido
    while True:
        try:
            valor = tipo(input(mensaje))
            return valor
        except ValueError:
            print("Entrada inválida. Por favor ingresa un número válido.")

def pedir_operacion():
    #Pide al usuario elegir la operación a realizar
    print("\n--- Operaciones numéricas seguras ---")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    while True:
        opcion = input("Elige una opción (1-4): ")
        if opcion in ["1", "2", "3", "4"]:
            return opcion
        else:
            print("Opcion invalida")


while True:
    operacion = pedir_operacion()
    
    a = pedir_numero("Ingresa el primer número: ")
    b = pedir_numero("Ingresa el segundo número: ")

    try:
        if operacion == "1":
            resultado = un.suma_segura(a, b)
            print(f"Resultado: {resultado}")
        elif operacion == "2":
            resultado = un.resta_segura(a, b)
            print(f"Resultado: {resultado}")
        elif operacion == "3":
            resultado = un.multiplicacion_segura(a, b)
            print(f"Resultado: {resultado}")
        elif operacion == "4":
            # División segura: si b=0, se capturará la excepción
            resultado = un.division_segura(a, b)
            print(f"Resultado: {resultado}")
        
        # Preguntar si quiere realizar otra operación
        continuar = input("\n¿Deseas realizar otra operación? (s/n): ").strip().lower()
        if continuar != "s":
            print("Cerrando programa")
            break

    except ValueError as ve:
        print(f"Error de valor: {ve}. Intenta de nuevo.")
    except TypeError as te:
        print(f"Error de tipo: {te}. Intenta de nuevo.")
