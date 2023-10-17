def multiplica_lista(lista):
    resultado = 1
    for numero in lista:
        resultado *= numero
    return resultado

# Ejemplo de uso
lista = [8, 2, 3, -1, 7]
resultado = multiplica_lista(lista)
print("Resultado de la multiplicación:", resultado)
