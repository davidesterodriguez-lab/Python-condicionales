minimo = float(input("Ingrese el valor mínimo del intervalo: "))
maximo = float(input("Ingrese el valor máximo del intervalo: "))
x = float(input("Ingrese un número: "))

if minimo <= x <= maximo:
    print("El número está dentro del intervalo")
else:
    print("El número está fuera del intervalo")
