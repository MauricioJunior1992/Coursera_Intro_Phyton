
def fatorial(num):
    fator = 1
    while num > 1:
        fator = fator * num
        num -= 1
    print(fator)
    num = int(input("Digite um número inteiro: "))
    return num

num = int(input("Digite um número inteiro: "))
while num >= 0:
    num = fatorial(num)