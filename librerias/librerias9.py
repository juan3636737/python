n = int(input("Número de votos: "))

votos_candidato1 = 0
votos_candidato2 = 0
votos_candidato3 = 0
votos_blancos = 0
votos_nulos = 0

for _ in range(n):
    voto = int(input("Voto (1 para Candidato 1, 2 para Candidato 2, 3 para Candidato 3, 0 para Blanco, otros para Nulo): "))
    if voto == 1:
        votos_candidato1 += 1
    elif voto == 2:
        votos_candidato2 += 1
    elif voto == 3:
        votos_candidato3 += 1
    elif voto == 0:
        votos_blancos += 1
    else:
        votos_nulos += 1

print(f"Votos para Candidato 1: {votos_candidato1}")
print(f"Votos para Candidato 2: {votos_candidato2}")
print(f"Votos para Candidato 3: {votos_candidato3}")
print(f"Votos en blanco: {votos_blancos}")
print(f"Votos nulos: {votos_nulos}")
