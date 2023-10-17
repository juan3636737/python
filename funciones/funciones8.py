def contar_letras(cadena):
    mayusculas = sum(1 for letra in cadena if letra.isupper())
    minusculas = sum(1 for letra in cadena if letra.islower())
    return mayusculas, minusculas
