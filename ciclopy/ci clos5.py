
numero = int(input("Ingrese un número entero para ver su tabla de multiplicar: "))
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    producto = numero * i
    print(f"{numero} x {i} = {producto}")
