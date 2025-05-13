#3. Perímetro y área de un rectángulo**
def calcular_perimetro_y_area():
    try:
        largo = float(input("Introduce el largo del rectángulo: "))
        ancho = float(input("Introduce el ancho del rectángulo: "))
    
        if largo <= 0 or ancho <= 0:
            print("El largo y el ancho deben ser valores positivos.")
            return
        area = largo * ancho
        perimetro = 2 * (largo + ancho)
        print(f"El área del rectángulo es: {area:.2f}")
        print(f"El perímetro del rectángulo es: {perimetro:.2f}")
    
    except ValueError:
        print("Por favor, introduce valores numéricos válidos.")
calcular_perimetro_y_area()
