#Preguntar al usuario el nombre y la edad, si es mayor o igual a 18 años mostrar el mensaje 
#"Usted es mayor de edad", de lo contrario "Usted es menor de edad". Si el número ingresado es 
#negativo o la edad ingresada es mayor a 100 años, mostrar al usuario un mensaje de ingresar una edad válida.
nombre = str(input("ingrese su nombre: "))
numero = int(input("Ingrese su edad: "))

# Determinar si es par, impar o cero
if numero <= 0:
    print(f" {nombre} usted no ha nacido.")
elif numero >=18:
    print(f" {nombre} usted es mayor de edad")
else:
    print(f" {nombre} usted es meno0r de edad .")
