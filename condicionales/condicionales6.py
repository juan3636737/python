#Crear un programa con un menú de opciones, que permita calcular 
#las áreas de figuras geométricas (cuadrado, rectángulo, triángulo, círculo, rombo y trapecio)
menu = """
 1-rectangulo
 2-cuadrado
 3-paralelogramo
 4-rombo
 5-trapecio
 6-triangulo
 7-triangulo equilatero
 8-triangulo rectangulo
 9-poligono regular
 """
opcion = input(menu)
if opcion == "1":
    numero = int(input("Ingrese el ancho de su rectangulo: "))
    numero1 = int(input("Ingrese el largo de su rectangulo: "))
    total = numero * numero1
    print("el area de este rectangulo es de {total}")
elif opcion == "2":
    numero = int(input("Ingrese un lado de el cuadrado: "))
    total = numero * numero
    print("el area de este cuadrado es de {total}")
elif opcion == "3":
    numero = int(input("Ingrese la base de este paralelogramo: "))
    numero1 = int(input("Ingrese la altura de este paralelogramo: "))
    total = numero * numero1
    print("el area de este paralelogramo es de {total}")
elif opcion == "5":
    numero = int(input("Ingrese la base de este trapecio: "))
    numero1 = int(input("Ingrese la distancacia de la cresta: "))
    numero2 = int(input("Ingrese la altura: "))
    total1 = numero + numero1
    total2 = total1/2
    total = total2*numero2
    print("el area de este trapecio es de {total}")
elif opcion == "6":
    numero = int(input("Ingrese la base : "))
    numero1 = int(input("Ingrese la altura: "))
    total1 = numero * numero1
    total = total1/2
    print("el area de este triangulo es de {total}")
elif opcion == "7":
    numero= int(input("ingrese un lado de el triangulo"))
    total1 =numero*numero
    total2 =total1*1.73205081
    total = total2/4
    print("el area de este triangulo es de {total}")
elif opcion == "8":
     numero = int(input("Ingrese la base : "))
     numero1 = int(input("Ingrese la altura: "))
     total1 = numero * numero1
     total = total1/2
     print("el area de este triangulo rectangulo es de {total}")
elif opcion == "9":