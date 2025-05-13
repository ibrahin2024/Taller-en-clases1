#6alcular interés compuesto**
def calcular_interes_compuesto():
    try:
        
        P = float(input("Introduce el capital inicial (P): "))
        r = float(input("Introduce la tasa de interés anual (en %): ")) / 100  
        t = int(input("Introduce el número de años (t): "))
        n = int(input("Introduce el número de veces que se capitaliza el interés al año (n): "))

        A = P * (1 + r / n) ** (n * t)

        print(f"El monto final después de {t} años es: {A:.2f}")
    
    except ValueError:
        print("Por favor, ingresa valores numéricos válidos.")

calcular_interes_compuesto()
