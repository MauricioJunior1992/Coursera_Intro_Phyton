soma = int(input("Digite o primeiro número: "))
resp = "S"

while resp == "S" or resp =="s":
    num2 = int(input("Digite o número a ser somado: "))
    soma += num2
    resp = input("Continuar somando? (S) ou (N): ")

print ("A soma de todos os número é", soma)