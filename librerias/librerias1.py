datos = input("Ingrese una lista de números separados por espacios: ")
numeros = [int(x) for x in datos.split()]
maximo = max(numeros)
print("El número más grande es:", maximo)
