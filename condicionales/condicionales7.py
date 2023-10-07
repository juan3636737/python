menu = """
Opciones de conversión:
1. Fahrenheit a Celsius
2. Fahrenheit a Kelvin
3. Fahrenheit a Rankine
4. Fahrenheit a Réaumur
5. Celsius a Fahrenheit
6. Celsius a Kelvin
7. Celsius a Rankine
8. Celsius a Réaumur
9. Kelvin a Celsius
10. Kelvin a Fahrenheit
11. Kelvin a Rankine
12. Kelvin a Réaumur
13. Rankine a Celsius
14. Rankine a Fahrenheit
15. Rankine a Kelvin
16. Rankine a Réaumur
17. Réaumur a Celsius
18. Réaumur a Fahrenheit
19. Réaumur a Kelvin
20. Réaumur a Rankine
21. Salir
"""

while True:
    print(menu)
    opcion = input("Elija una opción: ")

    if opcion == "21":
        break

    temperatura = float(input("Ingrese la temperatura a convertir: "))

    if opcion == "1":
        resultado = (temperatura - 32) / 1.8
        unidad_destino = "Celsius"
    elif opcion == "2":
        resultado = (temperatura + 459.67) / 1.8
        unidad_destino = "Kelvin"
    elif opcion == "3":
        resultado = temperatura + 459.67
        unidad_destino = "Rankine"
    elif opcion == "4":
        resultado = (temperatura - 32) / 2.25
        unidad_destino = "Réaumur"
    elif opcion == "5":
        resultado = temperatura * 1.8 + 32
        unidad_destino = "Fahrenheit"
    elif opcion == "6":
        resultado = temperatura + 273.15
        unidad_destino = "Kelvin"
    elif opcion == "7":
        resultado = temperatura * 1.8 + 32 + 459.67
        unidad_destino = "Rankine"
    elif opcion == "8":
        resultado = temperatura * 0.8
        unidad_destino = "Réaumur"
    elif opcion == "9":
        resultado = temperatura - 273.15
        unidad_destino = "Celsius"
    elif opcion == "10":
        resultado = temperatura * 1.8 - 459.67
        unidad_destino = "Fahrenheit"
    elif opcion == "11":
        resultado = temperatura * 1.8
        unidad_destino = "Rankine"
    elif opcion == "12":
        resultado = (temperatura - 273.15) * 0.8
        unidad_destino = "Réaumur"
    elif opcion == "13":
        resultado = (temperatura - 32 - 459.67) / 1.8
        unidad_destino = "Celsius"
    elif opcion == "14":
        resultado = temperatura - 459.67
        unidad_destino = "Fahrenheit"
    elif opcion == "15":
        resultado = temperatura / 1.8
        unidad_destino = "Kelvin"
    elif opcion == "16":
        resultado = (temperatura - 32 - 459.67) / 2.25
        unidad_destino = "Réaumur"
    elif opcion == "17":
        resultado = temperatura * 1.25
        unidad_destino = "Celsius"
    elif opcion == "18":
        resultado = temperatura * 2.25 + 32
        unidad_destino = "Fahrenheit"
    elif opcion == "19":
        resultado = temperatura * 1.25 + 273.15
        unidad_destino = "Kelvin"
    elif opcion == "20":
        resultado = temperatura * 2.25 + 32 + 459.67
        unidad_destino = "Rankine"
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

    print(f"{temperatura} grados {unidad_destino} son equivalentes a {resultado} grados {unidad_destino}")
