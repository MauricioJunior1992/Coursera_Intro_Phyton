
def inverte_lista(lista):
    i = 0
    while i < len(lista)//2:
        aux = lista[i]
        lista[i] = lista[(-i)-1]
        lista[(-i)-1] = aux
        i += 1
    del lista[0]
    return lista

lista = [int(input("Digite um número inteiro: "))]
i = 0
while lista[i] != 0:
    lista.append(int(input("Digite um número inteiro: ")))
    i += 1

print(inverte_lista(lista))