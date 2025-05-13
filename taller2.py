#2. Conversión de temperatura (Celsius a Fahrenheit o Fahrenheit a Celsius)**
def convertir_temperatura():
    print("Selecciona la conversión que deseas realizar:")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    
    opcion = input("Ingresa el número de la opción (1 o 2): ")
    
    if opcion == "1":
        celsius = float(input("Ingresa la temperatura en Celsius: "))
        fahrenheit = (9 / 5) * celsius + 32
        print(f"{celsius}°C es igual a {fahrenheit:.2f}°F")
    
    elif opcion == "2":
        fahrenheit = float(input("Ingresa la temperatura en Fahrenheit: "))
        celsius = (5 / 9) * (fahrenheit - 32)
        print(f"{fahrenheit}°F es igual a {celsius:.2f}°C")
    
    else:
        print("Opción no válida. Por favor, elige 1 o 2.")
convertir_temperatura()
