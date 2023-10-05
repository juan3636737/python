#Calcular la hipotenusa con el Teorema de Pitágoras.
num1 = float(input("Ingrese un lado, ya sabemos que el numero esta elevado al cuadrado "))
num2 = float(input("Ingrese un lado, ya sabemos que el numero esta elevado al cuadrado "))
total1 = num1*num1
total2 = num2*num2
total3 = total1+total2
total = total3 ** 0.5
print(f"la hipotenusa es: {total}")