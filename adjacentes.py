# Verificar se existem dois números iguais adjacentes na sequência

adjacente = False
sequencia = input("Digite um número inteiro: ")
tamanho = len(sequencia)
i = 0
sequencia = int(sequencia)
numAnterior = -1
divRest = 10
divInt = 1

while i < tamanho and adjacente == False:
    numAtual = (sequencia % divRest) // divInt
    if numAnterior != numAtual:
        numAnterior = numAtual
        divInt *= 10
        divRest *= 10
        i += 1
    else:
        adjacente = True
        
if adjacente == True:
    print("sim")
else:
    print("não")