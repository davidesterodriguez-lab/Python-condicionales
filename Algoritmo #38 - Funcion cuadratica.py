a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

if b**2 - 4*a*c >= 0 and a != 0:
    print("La función cuadrática sí tiene solución")
else:
    print("La función cuadrática no tiene solución")
