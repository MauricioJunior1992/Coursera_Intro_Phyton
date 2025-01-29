
def n_primos(num):

    i = 1
    qntPrimos = 0
    while i <= num:
        primo = True
        j = 1
        div = 2
        while j < (i - 1) and primo == True:
            if i % div != 0:
                j += 1
                div += 1
            else:
                primo = False
        if j == (i - 1) and primo == True:
            qntPrimos += 1
        i += 1
    return qntPrimos