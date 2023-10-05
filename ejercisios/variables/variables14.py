#Solicitar al usuario una distancia en metros y transformar a km., cm. o mm
num1 = float(input("Ingrese la distacia que desea convertir teniendo  en cuenta que la distancia que ingresa esta en metros "))

total2 =num1/100
total1 = num1*1000
total3 = num1/1000
print(f"el la distancia en km es de: {total1} km, la distancia en cm es de: {total2} cm y la distancia en mm es de: {total3} mm")