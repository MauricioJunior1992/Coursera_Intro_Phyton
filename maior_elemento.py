
def maior_elemento(lista):
    maior = 0
    for num in lista:
        i = 0
        while i < len(lista):
            if num > lista[i]:
                maior = num
                break
            else:
                i += 1
    return maior

lista = [1,2,4,5,10,89]
print(maior_elemento(lista))