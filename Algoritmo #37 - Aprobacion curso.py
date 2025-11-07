nota1 = float(input("Ingrese la nota del trabajo #1: "))
nota2 = float(input("Ingrese la nota del trabajo #2: "))
nota3 = float(input("Ingrese la nota del trabajo #3: "))
nota4 = float(input("Ingrese la nota del trabajo #4: "))

if (nota1 + nota2 + nota3 + nota4) / 4 >= 3.5:
    print("Usted aprobó el curso")
else:
    print("Usted reprobó el curso")
