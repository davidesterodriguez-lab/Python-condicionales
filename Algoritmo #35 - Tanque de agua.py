litros = int(input("Ingrese la cantidad de litros que tiene el tanque: "))

if litros < 250:
    print("La llave debe estar abierta.")
elif 250 <= litros <= 450:
    print("La llave debe estar cerrada.")
else:
    print("La llave debe estar cerrada.")
