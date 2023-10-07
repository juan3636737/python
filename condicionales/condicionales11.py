print("Tamaños de pizza disponibles:")
print("1. Tamaño 1 - $15000")
print("2. Tamaño 2 - $24000")
print("3. Tamaño 3 - $36000")

opcion = int(input("Seleccione el tamaño de la pizza (1/2/3): "))
ingrediente = int(input("ingrese cuantos ingredientes adicionales desea:"))
tamaño1 = 15000
tamaño2 = 24000
tamaño3 = 36000
tingre = ingrediente * 4000
ttamaño1 = 15000 + tingre
ttamaño2 = 24000 + tingre
ttamaño3 = 36000 + tingre

if opcion == 1:
     print(f"el precio de la pizza tamaño1 es de: {ttamaño1}") 
elif opcion == 2:
     print(f"el precio de la pizza tamaño2 es de: {ttamaño2}") 
elif opcion == 3:
     print(f"el precio de la pizza tamaño3 es de: {ttamaño3}")  
else:
      print("Opción no válida")