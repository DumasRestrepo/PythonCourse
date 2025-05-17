def bubble_sort(lista):
    lista = lista.copy()
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                temp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temp

    return lista

# Lista original
lista = [12, 3, 4, 1, 6, 10]
print("Lista ordenada:", bubble_sort(lista))  # Devuelve lista ordenada
print("Lista original:", lista)  # Verifica que la original no fue modificada
