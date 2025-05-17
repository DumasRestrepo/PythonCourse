def contar_letras(texto):
    conteo = {}
    for letra in texto.lower():
        if letra != '':
            conteo[letra] = conteo.get(letra, 0) + 1
    return conteo

print(contar_letras('Ana'))
