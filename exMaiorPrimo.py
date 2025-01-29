def maior_primo(num):
    div = 2
    i = 1
    j = 1
    maiorPrimo = 0
    while i <= num:
        primo = True
        div = 2
        j = 1
        while j < (i-1) and primo == True:
            if i % div != 0:
                div += 1
                j += 1
            else:
                primo = False
        if primo == True:
            maiorPrimo = i
        i += 1
    if num == 2:
        maiorPrimo = 2
    return maiorPrimo

num = int(input("Digite um número inteiro: "))

print(maior_primo(num))