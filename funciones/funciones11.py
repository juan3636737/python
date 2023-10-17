def numeros_pares(lista):
    pares = [num for num in lista if num % 2 == 0]
    return pares

# Ejemplo de uso
lista = [1, 2, 3, 4, 5, 6, 7, 8]
pares = numeros_pares(lista)
print("Números pares:", pares)
