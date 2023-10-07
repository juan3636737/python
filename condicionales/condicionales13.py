
peso = float(input("Ingrese el peso en kg: "))
estatura = float(input("Ingrese la estatura en metros: "))
imc = peso / (estatura ** 2)
if imc < 18.5:
    estado = "Desnutrido"
elif imc >= 18.5 and imc < 25:
    estado = "Normal"
elif imc >= 25 and imc < 30:
    estado = "Sobrepeso"
elif imc >= 30 and imc < 35:
    estado = "Obesidad Grado 1"
elif imc >= 35 and imc < 40:
    estado = "Obesidad Grado 2"
else:
    estado = "Obesidad Grado 3"


print(f"El IMC es: {imc}")
print(f"Estado de salud: {estado}")
