
def retangulo(alt, larg):
    i = 1
    while i <= alt:
        j = 1
        while j <= larg:
            print("#", end = "")
            j += 1
        i += 1
        print("")

larg = int(input("digite a largura: "))
alt = int(input("digite a altura: "))

retangulo(alt, larg)