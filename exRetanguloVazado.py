def retangulo(alt, larg):
    i = 1
    while i <= alt:
        j = 1
        if i == 1 or i == alt:
            while j <= larg:
                print("#", end = "")
                j += 1
        else:
            while j <= larg:
                if j == 1 or j == larg:
                    print("#", end = "")
                else:
                    print(" ", end = "")
                j += 1
        i += 1
        print("")

larg = int(input("digite a largura: "))
alt = int(input("digita a altura: "))

retangulo(alt, larg)

