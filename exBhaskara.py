import math

a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

delta = (b ** 2) - (4 * a * c)

if delta == 0:
    x = (b*-1) / (2*a)
    print("a raiz desta equação é", x)

elif delta < 0:
    print("esta equação não possui raízes reais")

else:
    raizDelta = math.sqrt(delta)
    x1 = ((b*-1) + raizDelta) / (2*a)
    x2 = ((b*-1) - raizDelta) / (2*a)
    if x1 > x2:
        print("as raízes da equação são", x2, "e", x1)
    else:
        print("as raízes da equação são", x1, "e", x2)

