from queue import Queue, LifoQueue


class Nodo:
    def __init__(self, estado, pai, acao, custo):
        """
        Inicializa o nodo com os atributos recebidos
        :param estado:str, representacao do estado do 8-puzzle
        :param pai:Nodo, referencia ao nodo pai, (None no caso do nó raiz)
        :param acao:str, acao a partir do pai que leva a este nodo (None no caso do nó raiz)
        :param custo:int, custo do caminho da raiz até este nó
        """
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo


def troca(palavra, a, b):
    palavra = list(palavra)
    palavra[a], palavra[b] = palavra[b], palavra[a]
    return ''.join(palavra)


def sucessor(estado):
    """
    Recebe um estado (string) e retorna uma lista de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:
    :return:
    """
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


def move_cima(estado, posicao):
    if pode_mover_cima(estado, posicao):
        return troca(estado, posicao, posicao-3)
    else:
        return estado


def move_baixo(estado, posicao):
    if pode_mover_baixo(estado, posicao):
        return troca(estado, posicao, posicao+3)
    else:
        return estado


def move_direita(estado, posicao):
    if pode_mover_direita(estado, posicao):
        return troca(estado, posicao, posicao+1)
    else:
        return estado


def move_esquerda(estado, posicao):
    if pode_mover_esquerda(estado, posicao):
        return troca(estado, posicao, posicao-1)
    else:
        return estado


def expande(nodo):
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um iterable de nodos.
    Cada nodo do iterable é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    """
    nodos_filhos = []
    pai = nodo
    jogadas = sucessor(nodo.estado)
    for jogada in jogadas:
        nodos_filhos.append(Nodo(jogada[1], pai, jogada[0], pai.custo+1))
    return nodos_filhos


def bfs(estado):
    """
    Recebe um estado (string), executa a busca em LARGURA e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    objetivo = "12345678_"
    caminho = []
    x = set()
    f: Queue = Queue()
    f.put(Nodo(estado, None, None, 0))
    while (not f.empty()):
        v = f.get()
        if v.estado == objetivo:
            while v.pai is not None:
                caminho.insert(0, v)
                v = v.pai
            return caminho
        if v.estado not in x:
            x.add(v.estado)
            for z in expande(v):
                f.put(z)
    return None


def dfs(estado):
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    objetivo = "12345678_"
    caminho = []
    x = set()
    f: LifoQueue = LifoQueue()
    f.put(Nodo(estado, None, None, 0))
    while (not f.empty()):
        v = f.get()
        if v.estado == objetivo:
            while v.pai is not None:
                caminho.insert(0, v)
                v = v.pai
            return caminho
        if v.estado not in x:
            x.add(v.estado)
            for z in expande(v):
                f.put(z)
    return None


def astar_hamming(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def astar_manhattan(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError
