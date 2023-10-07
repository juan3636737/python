
numero = int(input("Ingrese el número de llantas compradas: "))

precio_menos_seis = 240000
precio_seis_siete = 221000
precio_mas_siete = 180000


if numero < 6:
    total = numero * precio_menos_seis
elif numero >= 6 and numero <= 7:
    total = numero * precio_seis_siete
else:
    total = numero * precio_mas_siete


print("El valor total a pagar por", numero, "llantas es de $", total)
