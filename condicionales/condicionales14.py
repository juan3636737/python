
edad = int(input("Ingrese la edad: "))
genero = input("Ingrese el género (1 para femenino, 2 para masculino): ")
genero = int(genero)


if genero == 1:
    pulsaciones = (220 - edad) / 10
elif genero == 2:
    pulsaciones = (210 - edad) / 10 

if pulsaciones :
    print(f"El número de pulsaciones por cada 10 segundos de ejercicio es: {pulsaciones}")
