#Programa que permita a una tienda saber el valor que pagara un cliente por la compra
#de varios elementos de la misma referencia. Debe tener como entradas el valor unitario,
#la cantidad de productos comprados y al valor final se debe adicionar el 16% correspondiente al IVA.
num1 = float(input("Ingrese el valor del producto: "))
num2 = float(input("Ingrese la cantidad: "))
producto= num1*num2
iva= producto*0.16
total= producto+iva
print(f"el valor unitario del producto es: {num1} la cantidad de produtos son {num2}\n el valor de los produtos es de {producto} y el valor total es de {total}")