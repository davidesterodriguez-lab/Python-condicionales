nombre = (str(input("Ingrese su nombre: ")))
edad = (int(input("Ingrese su edad: ")))

if edad >= 18:
    mensajeEdad = "mayor de edad"
else:
    mensajeEdad = "menor de edad"

print("Hola ", nombre, " usted es ", mensajeEdad)