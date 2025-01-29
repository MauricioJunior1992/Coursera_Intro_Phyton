num = input("Digite um número inteiro: ")
tamanho = len(num)
num = int(num)
divInt = 1
divRest = 10
soma = 0
i = 0

while i < tamanho:
    numAux = (num % divRest) // divInt
    soma += numAux
    divInt *= 10
    divRest *= 10
    i += 1

print(soma)