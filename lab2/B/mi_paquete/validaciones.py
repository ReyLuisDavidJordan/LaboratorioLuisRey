def requiere_positivo(*args):
    for i, valor in enumerate(args):
        if valor <= 0:
            raise ValueError(f"El argumento en posición {i} ({valor}) debe ser mayor a 0")
