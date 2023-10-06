#Solicitar dos números al usuario y calcular cuál es el mayor y cuál el menor, e imprimir el resultado.

numero = int(input("Ingrese un número: "))
numero1 = int(input("Ingrese un número: "))

if numero1 < numero :
    print(f"El número {numero} es mayor que {numero1}")
elif numero1 > numero:
    print(f"El número {numero1} es mayor que {numero}")