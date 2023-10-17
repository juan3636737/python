def obtener_digitos_binarios(numero):
    digitos_binarios = []
    while numero > 0:
        residuo = numero % 2
        digitos_binarios.insert(0, residuo)
        numero = numero // 2
    return digitos_binarios

numero = int(input("Ingrese un número entero: "))
binario = obtener_digitos_binarios(numero)
print("Representación binaria:", binario)
