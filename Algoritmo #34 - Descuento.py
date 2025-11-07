valor1 = float(input("Ingrese el valor del producto: "))

if valor1 > 150000:
    print("El valor del descuento es:", valor1 - (valor1 * 0.95))
else:
    print("El valor del descuento es: 0")
