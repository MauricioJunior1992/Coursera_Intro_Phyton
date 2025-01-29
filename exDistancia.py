import math

x1 = float(input("Coordenada X do primeiro ponto: "))
y1 = float(input("Coordenada y do primeiro ponto: "))
x2 = float(input("Coordenada X do segundo ponto: "))
y2 = float(input("Coordenada X do segundo ponto: "))

x = (x1 - x2) ** 2
y = (y1 - y2) ** 2

if math.sqrt(x+y) > 10:
    print("longe")
else:
    print("perto")