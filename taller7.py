#7. Cálculo del promedio de N notas**
total_notas = 0
cantidad_notas = 0

while True:
    entrada = input("Ingresa una nota (o escribe 'fin' para terminar): ")
    
    if entrada.lower() == 'fin':
        break
    
    try:
        nota = float(entrada)
        
        if nota < 0:
            print("Las notas no pueden ser negativas. Intenta nuevamente.")
            continue
        total_notas += nota
        cantidad_notas += 1
    except ValueError:
        print("Por favor, ingresa un valor numérico válido.")
    
if cantidad_notas > 0:
    promedio = total_notas / cantidad_notas
    print(f"El promedio de las {cantidad_notas} notas ingresadas es: {promedio:.2f}")
else:
    print("No se ingresaron notas.")
