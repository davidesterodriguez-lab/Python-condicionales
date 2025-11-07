tipo = input("Ingrese el tipo del producto: ")
valor1 = float(input("Ingrese el valor del producto: "))

if tipo == "1":
    descuento = 0.125
elif tipo == "2":
    descuento = 0.83
elif tipo == "3":
    descuento = 0.83
elif tipo == "4":
    descuento = 0.32
else:
    descuento = 1

valorfinal = valor1 * descuento
print("Este es el valor final del producto:", valorfinal)
