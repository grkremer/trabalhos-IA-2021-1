from typing import Tuple


def troca(palavra, a, b):
    palavra = list(palavra)
    palavra[a], palavra[b] = palavra[b], palavra[a]
    return ''.join(palavra)

def sucessor(estado):
    posicao = acha_underline(estado)
    return ( move_esquerda(estado,posicao), move_direita(estado,posicao), move_cima(estado,posicao), move_baixo(estado, posicao) )

def acha_underline(estado):
    return estado.index('_')

def move_cima(estado,posicao):
    if posicao-3 >= 0:
        return troca(estado, posicao, posicao-3)
    else:
        return ''

def move_baixo(estado,posicao):
    if posicao+3 < 9:
        return troca(estado, posicao, posicao+3)
    else:
        return ''

def move_direita(estado,posicao):
    if posicao != 2 and posicao != 5 and posicao != 8:
        return troca(estado, posicao, posicao+1)
    else:
        return ''

def move_esquerda(estado,posicao):
    if posicao != 0 and posicao != 3 and posicao != 6:
        return troca(estado, posicao, posicao-1)
    else:
        return ''


def print_estado(estado):
    print(estado[0:3])
    print(estado[3:6])
    print(estado[6:9])

caso = "12_345678"
print_estado(caso)
print("___")
print(sucessor(caso))






