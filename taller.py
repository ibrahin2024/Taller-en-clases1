#1. Área y perímetro de un círculo**
import math

def calcular_area_y_perimetro():
    try:
        radio = float(input("Introduce el radio del círculo: "))
        
        if radio <= 0:
            print("El radio debe ser un valor positivo.")
            return
        area = math.pi * radio**2
        perimetro = 2 * math.pi * radio
        
        print(f"El área del círculo es: {area:.2f}")
        print(f"El perímetro del círculo es: {perimetro:.2f}")
    
    except ValueError:
        print("Por favor, introduce un valor numérico válido.")

calcular_area_y_perimetro()
