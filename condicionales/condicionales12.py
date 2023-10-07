
cantidad = int(input("Ingrese la cantidad de producutos: "))
unitario = float(input("Ingrese el precio unitario : "))

if cantidad <= 5:
    descuento = 0
elif cantidad < 10:
    descuento = 0.05  
else:
    descuento = 0.08  

subtotal = cantidad * unitario
descuentoo = subtotal * descuento
total = subtotal - descuentoo

print(f"Valor total a pagar con descuento: ${total}")
