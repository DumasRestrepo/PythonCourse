def contar(palabra)->dict:
    contador = {}
    for letra in palabra.lower():
        if letra != " ":
            contador[letra] = contador.get(letra, 0) + 1
    return contador

print(contar("Hola Mundo"))