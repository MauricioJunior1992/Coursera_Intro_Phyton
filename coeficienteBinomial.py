def fatorial(num):
    fator = 1
    while num > 1:
        fator = fator * num
        num -= 1
    return fator

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
while num2 > num1:
    num2 = int(input("O segundo número precisa ser menor ou igual ao primeiro: "))

binomial = (fatorial(num1)/(fatorial(num2)*fatorial(num1-num2)))

print(binomial) 
