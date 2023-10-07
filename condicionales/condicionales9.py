
numero = float(input("Ingrese el monto de la cuenta: "))


if numero < 150000:
    pago = "Pago en Efectivo"
elif numero >= 150000 and numero <= 300000:
    pago = "Pago con el Celular (Dinero Electrónico)"
elif numero > 300000 and numero <= 600000:
    pago = "Pago con Tarjeta de Débito"
else:
    pago = "Pago con Tarjeta de Crédito"

print("Se recomienda realizar un", pago)
