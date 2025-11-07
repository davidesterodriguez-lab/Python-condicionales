valor1 = float(input("Ingrese el valor del artículo: "))
tipo = input("Ingrese el tipo del artículo (textil = 1, electrodoméstico = 2, elementos de cocina = 3, o videojuego = 4): ")

if tipo == "1":
    print("El valor del descuento es:", valor1 - (valor1 * 0))
elif tipo == "2":
    print("El valor del descuento es:", valor1 * 0.037)
elif tipo == "3":
    print("El valor del descuento es:", valor1 * 0.042)
elif tipo == "4":
    print("El valor del descuento es:", valor1 * 0.078)
else:
    print("Tipo de artículo inválido")
