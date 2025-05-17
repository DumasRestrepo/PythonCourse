def ordenamiento_burbuja(lista):
    lista = lista.copy()
    tamano_lista = len(lista) #
    for i in range(tamano_lista):
        for j in range(0, tamano_lista -i - 1):
            if lista[j] > lista[j+1]:
                temp = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temp
    return lista

    

if __name__ == '__main__':
    print("ALGORITMO DE ORDENAMIENTO")
    valores_inmuebles = [4,6,1,2] # Todos los valores estan en doalres
    print(valores_inmuebles)
    valores_ordenados = ordenamiento_burbuja(valores_inmuebles)
    print(valores_ordenados) #Lista ordenada
    print(valores_inmuebles) # Lista no ordenada
