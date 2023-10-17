
import random

lanzamientos = 0

while True:
    lanzamientos += 1
    resultado = random.randint(1, 6)
    if resultado == 5:
        break

print(f"Se necesitaron {lanzamientos} lanzamientos para obtener un 5.")
