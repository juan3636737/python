import random

n = int(input("Número de lanzamientos del dado: "))
contador_tres = 0

for _ in range(n):
    resultado = random.randint(1, 6)
    if resultado == 3:
        contador_tres += 1

print(f"El número 3 se obtuvo {contador_tres} veces en {n} lanzamientos.")
