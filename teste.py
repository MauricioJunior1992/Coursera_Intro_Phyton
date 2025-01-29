import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = 4.5
    ttr = 0.7
    hlr = 0.55
    sal = 70.8
    sac = 1.8
    pal = 38.5

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(textos):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    i = 0
    while i < len(textos):
        sentencas = re.split(r'[.!?]+', textos[i])
        if sentencas[-1] == '':
            del sentencas[-1]
        i += 1
    return sentencas

def separa_frases(sentencas):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    i = 0
    frases = []
    while i < len(sentencas):
        frases.append(re.split(r'[,:;]+', sentencas[i]))
        i += 1
    return frases

def separa_palavras(frases):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    i = 0
    palavras = []
    for palavra in frases:
        palavras.append(palavra[i].split())
        i += 1
    return palavras

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    pass

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''

    wal = 4.5
    ttr = 0.7
    hlr = 0.55
    sal = 70.8
    sac = 1.8
    pal = 38.5

    pass

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    pass

le_assinatura()
texto = le_textos()
sentencas = separa_sentencas(texto)
print("Sentenças: ", sentencas)
frases = separa_frases(sentencas)
print("Frases: ", frases)
palavras = separa_palavras(frases)
print("Palavras: ", palavras)
print("Palavras únicas: ", n_palavras_unicas(palavras))
print("Palavras diferentes: ", n_palavras_diferentes(palavras))