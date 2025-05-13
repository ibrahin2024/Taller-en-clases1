#8. Cálculo de descuento con validación**
while True:
    try:
        precio_original = float(input("Ingresa el precio original del producto: "))
        if precio_original < 0:
            print("El precio no puede ser negativo. Intenta nuevamente.")
            continue
        break
    except ValueError:
        print("Por favor, ingresa un valor numérico válido para el precio.")

while True:
    try:
        porcentaje_descuento = float(input("Ingresa el porcentaje de descuento (0-100): "))
        
        if porcentaje_descuento < 0 or porcentaje_descuento > 100:
            print("El porcentaje de descuento debe estar entre 0 y 100. Intenta nuevamente.")
            continue
        break
    except ValueError:
        print("Por favor, ingresa un valor numérico válido para el porcentaje de descuento.")

descuento = (precio_original * porcentaje_descuento) / 100
precio_final = precio_original - descuento

print(f"El precio original del producto es: ${precio_original:.2f}")
print(f"El descuento aplicado es: ${descuento:.2f}")
print(f"El precio final después del descuento es: ${precio_final:.2f}")
