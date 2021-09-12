
def troca(palavra, a, b):
    palavra = list(palavra)
    palavra[a], palavra[b] = palavra[b], palavra[a]
    return ''.join(palavra)

def sucessor(estado):
    posicao = acha_underline(estado)
    solucoes = []
    if(pode_mover_baixo(estado, posicao)):
        solucoes.append(("abaixo", move_baixo(estado, posicao)))
    if(pode_mover_cima(estado, posicao)):
        solucoes.append(("acima", move_cima(estado, posicao)))
    if(pode_mover_esquerda(estado, posicao)):
        solucoes.append(("esquerda", move_esquerda(estado, posicao)))
    if(pode_mover_direita(estado, posicao)):
        solucoes.append(("direita", move_direita(estado, posicao)))
    return solucoes

def acha_underline(estado):
    return estado.index('_')

def pode_mover_cima(estado, posicao):
    return posicao-3 >= 0

def pode_mover_baixo(estado, posicao):
    return posicao+3 < 9

def pode_mover_esquerda(estado, posicao):
    return posicao != 0 and posicao != 3 and posicao != 6

def pode_mover_direita(estado, posicao):
    return posicao != 2 and posicao != 5 and posicao != 8

def move_cima(estado,posicao):
    if pode_mover_cima(estado, posicao):
        return troca(estado, posicao, posicao-3)
    else:
        return estado

def move_baixo(estado,posicao):
    if pode_mover_baixo(estado, posicao):
        return troca(estado, posicao, posicao+3)
    else:
        return estado

def move_direita(estado,posicao):
    if pode_mover_direita(estado, posicao):
        return troca(estado, posicao, posicao+1)
    else:
        return estado

def move_esquerda(estado,posicao):
    if pode_mover_esquerda(estado, posicao):
        return troca(estado, posicao, posicao-1)
    else:
        return estado


def print_estado(estado):
    print(estado[0:3])
    print(estado[3:6])
    print(estado[6:9])

caso = "12_345678"
print_estado(caso)
print("___")
print(sucessor(caso))







