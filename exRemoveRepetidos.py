

def remove_repetidos(lista):
    i = 0
    while i < len(lista):
        j = i + 1
        while j < len(lista):
            if lista[j] != lista[i]:
                j += 1
            else:
                del lista[j]
        i += 1
    lista.sort()
    return lista

