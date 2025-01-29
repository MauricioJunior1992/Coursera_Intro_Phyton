
def computador_escolhe_jogada(pecasTotais, limPecas):
    i = 1
    pecasRetiradas = 0
    while i <= limPecas:
        if ((pecasTotais - i) % (limPecas + 1)) == 0:
            pecasRetiradas = i
            break
        else:
            i += 1
    return pecasRetiradas

def usuario_escolhe_jogada(pecasTotais, limPecas):
    pecasRetiradas = int(input("\nQuantas peças você vai tirar? "))
    while pecasRetiradas > limPecas or pecasRetiradas > pecasTotais:
        print("\nOops! Jogada inválida! Tente de novo.")
        pecasRetiradas = int(input("\nQuantas peças você vai tirar? "))
    return pecasRetiradas


def partida():
    pecasTotais = int(input("\nQuantas peças? "))
    limPecas = int(input("Limite de peças por jogada? "))
    while limPecas > pecasTotais:
        print("\nOops. O número limite deve ser menor que o total de peças.")
        limPecas = int(input("Limite de peças por jogada? "))

    if pecasTotais % (limPecas + 1) == 0:
        print("\nVocê começa!")
        compTurno = False
    else:
        print("\nComputador começa!")
        compTurno = True

    if compTurno == True:
        while pecasTotais > 0:
            compTurno = True
            pecasRetiradas = computador_escolhe_jogada(pecasTotais, limPecas)
            if pecasRetiradas == 1:
                print("\nO computador tirou uma peça.")
            else:
                print("\nO computador tirou " + str(pecasRetiradas) + " peças.")
            pecasTotais -= pecasRetiradas
            if pecasTotais > 1:
                print("Agora restam " + str(pecasTotais) + " peças no tabuleiro.")
            elif pecasTotais == 0:
                break
            else:
                print("Agora resta apenas uma peça no tabuleiro")

            compTurno = False
            pecasRetiradas = usuario_escolhe_jogada(pecasTotais, limPecas)
            if pecasRetiradas == 1:
                print("\nVocê tirou uma peça.")
            else:
                print("\nVocê tirou " + str(pecasRetiradas) + " peças.")
            pecasTotais -= pecasRetiradas
            if pecasTotais > 1:
                print("Agora restam " + str(pecasTotais) + " peças no tabuleiro.")
            elif pecasTotais == 0:
                break
            else:
                print("Agora resta apenas uma peça no tabuleiro")
            compTurno = True
    elif compTurno == False:
        while pecasTotais > 0:
            compTurno = False
            pecasRetiradas = usuario_escolhe_jogada(pecasTotais, limPecas)
            if pecasRetiradas == 1:
                print("\nVocê tirou uma peça.")
            else:
                print("\nVocê tirou " + str(pecasRetiradas) + " peças.")
            pecasTotais -= pecasRetiradas
            if pecasTotais > 1:
                print("Agora restam " + str(pecasTotais) + " peças no tabuleiro.")
            elif pecasTotais == 0:
                break
            else:
                print("Agora resta apenas uma peça no tabuleiro")

            compTurno = True
            pecasRetiradas = computador_escolhe_jogada(pecasTotais, limPecas)
            if pecasRetiradas == 1:
                print("\nO computador tirou uma peça.")
            else:
                print("\nO computador tirou " + str(pecasRetiradas) + " peças.")
            pecasTotais -= pecasRetiradas
            if pecasTotais > 1:
                print("Agora restam " + str(pecasTotais) + " peças no tabuleiro.")
            elif pecasTotais == 0:
                break
            else:
                print("Agora resta apenas uma peça no tabuleiro")
    
    if compTurno == True:
        print("Fim do jogo! O computador ganhou!")
    else:
        print("Fim do jogo! Você ganhou!")
    return compTurno

def campeonato():
    print("\nBem-vindo ao jogo do NIM! Escolha:")
    escolha = int(input("\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato "))

    if escolha == 1:
        print("\nVocê escolheu uma partida isolada!")
        partida()
    else:
        print("\nVocê escolheu um campeonato!")
        i = 1
        pontosComp = 0
        pontosUser = 0
        while i <= 3:
            print("\n**** Rodada " + str(i) + " ****")
            ponto = partida()
            if ponto == True:
                pontosComp += 1
            else:
                pontosUser += 1
            i += 1
        print("**** Final do Campeonato! ****\n")
        print("Placar: Você " + str(pontosUser) + " X " + str(pontosComp) + " Computador")

campeonato()