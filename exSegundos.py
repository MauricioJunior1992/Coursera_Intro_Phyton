aux = input ("Por favor, entre com o número de segundos que deseja converter: ")
qtdSegundos = int(aux)

dias = (qtdSegundos // 3600) // 24
horas = (qtdSegundos // 3600) % 24
minutos = (qtdSegundos % 3600) // 60
segundos = (qtdSegundos % 3600) % 60

print (dias,"dias,", horas, "horas,", minutos ,"minutos e", segundos ,"segundos.")