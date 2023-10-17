import math

def area_rectangulo(ancho, alto):
    return ancho * alto

def area_circulo(radio):
    return math.pi * (radio ** 2)

def area_triangulo(base, altura):
    return 0.5 * base * altura

# Ejemplo de uso
ancho_rectangulo = 5
alto_rectangulo = 10
radio_circulo = 4
base_triangulo = 6
altura_triangulo = 8

area1 = area_rectangulo(ancho_rectangulo, alto_rectangulo)
area2 = area_circulo(radio_circulo)
area3 = area_triangulo(base_triangulo, altura_triangulo)

print("Área del rectángulo:", area1)
print("Área del círculo:", area2)
print("Área del triángulo:", area3)
