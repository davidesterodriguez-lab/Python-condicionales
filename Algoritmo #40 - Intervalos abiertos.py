print("Recuerde que en cada intervalo el valor asignado de a debe ser menor a b, Ej: a1 > b1")

a1 = (float(input("Ingrese los valores del primer intervalo a1: ")))
b1 = (float(input("Ingrese los valores del primer intervalo b1: ")))
a2 = (float(input("Ingrese los valores del primer intervalo a2: ")))
b2 = (float(input("Ingrese los valores del segundo intervalo b2: ")))
a3 = (float(input("Ingrese los valores del primer intervalo a3: ")))
b3 = (float(input("Ingrese los valores del tercer intervalo b3: ")))

x = int(input("Ingrese un número entero: "))

if (a1 < x < b1) or (a2 < x < b2) or (a3 < x < b3):
    print("El número se encuentra dentro de algún intervalo")
else:
    print("El número se encuentra fuera de los tres intervalos")
