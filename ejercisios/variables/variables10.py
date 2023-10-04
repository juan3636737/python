#Programa que permita determinar el salario a pagar a un empleado, 
#teniendo como entradas el salario diario y el número de días trabajados. 
#Tenga en cuenta que al empleado se le debe descontar el 10% por concepto de pensión y 15% por concepto de salud.
num1 = float(input("Ingrese valor del dia del empleado: "))
num2 = float(input("Ingrese cuantos dias trabaja: "))
salario= num1*num2
pension= salario*0.10
pensiont= salario-pension
salud= salario*0.15
saludt= salario-salud
total=pensiont-salud
print(f"el valor del dia del trabajador sale en {num1} trabajo {num2} dias,\n su salario menos pension es de {pensiont}, su salario menos salud es de {saludt} \n y su salario final es de {total} ")