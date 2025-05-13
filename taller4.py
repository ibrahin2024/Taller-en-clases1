#4. Potencia de un número con opción de repetir**
def calcular_potencia():
    while True:
        try:
            base = float(input("Introduce la base: "))
            exponente = int(input("Introduce el exponente: "))
            resultado = base ** exponente
            print(f"{base} elevado a {exponente} es igual a {resultado:.2f}")
            
            repetir = input("¿Quieres realizar otro cálculo? (s/n): ").lower()
            
            if repetir != 's':
                print("Gracias por usar el programa. ¡Hasta luego!")
                break
        
        except ValueError:
            print("Por favor, ingresa valores válidos para la base y el exponente.")

calcular_potencia()
