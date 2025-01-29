num = int(input("Digite um número inteiro: "))
div = 2
i = 1
primo = True

while i < (num-1) and primo == True:
    if num % div != 0:
        i += 1
        div += 1
    else:
        primo = False

if num == 2:
    primo = True

if primo == True:
    print("primo")
else:
    print("não primo")