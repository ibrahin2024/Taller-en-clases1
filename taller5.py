#5. Conversión de millas a kilómetros y metros**
def convertir_millas():
    try:
        
        millas = float(input("Introduce la cantidad de millas: "))
        kilometros = millas * 1.60934
        metros = millas * 1609.34
        print(f"{millas} millas son equivalentes a {kilometros:.2f} kilómetros o {metros:.2f} metros.")
    
    except ValueError:
        print("Por favor, ingresa un valor numérico válido.")
convertir_millas()
