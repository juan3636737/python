#Solicitar notas de 0.0 a 5.0 a un estudiante y calcular promedio.  
#Mostrar como "Aprobó" si el promedio es mayor o igual a 3.0, o mostrar "No aprobó" si su nota es menor a 3.0
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))
num4 = float(input("Ingrese el cuarto numero: "))
num5 = float(input("Ingrese el quinto numero: "))
num_n = 5
producto = num1+num2+num3+num4+num5
producto1 = producto/num_n
 
if producto1 >= 3:
    print(f" su nota fue de {producto1} entonses aprobo")

elif producto1 < 3:
    print(f" su nota fue de {producto1} entonses reprovo")
