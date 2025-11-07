num = int(input("Ingrese un número entre 0 y 20: "))

if num in (1, 2, 3, 5, 7, 11, 13, 17, 19):
    print("Es un número primo")
elif num in (4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20):
    print("No es un número primo")
else:
    print("Numero invalido")

