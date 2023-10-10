
altura = 4
numero = 1
for i in range(1, altura + 1):

    for j in range(altura - i):
        print(" ", end=" ")
    for k in range(1, i + 1):
        print(numero, end=" ")
        numero += 1
    print()
