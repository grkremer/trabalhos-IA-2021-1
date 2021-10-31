from queue import Queue, LifoQueue
import time


class Nodo:
    def custo_hamming(self, estado):
        valor = 0
        objetivo = "12345678_"
        for index, x in enumerate(estado):
            if objetivo[index] != x:
                valor += 1

        return valor

    def encontra_pos_y(self, y, e):
        if y in e[0:3]:
            return 0
        elif y in e[3:6]:
            return 1
        else:
            return 2

    def encontra_pos_x(self, x, e):
        if x in [e[0], e[3], e[6]]:
            return 0
        elif x in [e[1], e[4], e[7]]:
            return 1
        else:
            return 2

    def custo_manhattan(self, estado):
        valor = 0
        objetivo = "12345678_"
        for index, x in enumerate(estado):
            x_dist = abs(self.encontra_pos_x(x, objetivo) -
                         self.encontra_pos_x(x, estado))
            y_dist = abs(self.encontra_pos_y(x, objetivo) -
                         self.encontra_pos_y(x, estado))
            valor += x_dist+y_dist
        return valor

    def calcula_custo_total(self):
        self.custo_total_manhattan = self.custo + \
            self.custo_manhattan(self.estado)
        self.custo_total_hamming = self.custo + self.custo_hamming(self.estado)

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
        self.custo_total_manhattan = 0
        self.custo_total_hamming = 0


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
                caminho.insert(0, v.acao)
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
                caminho.insert(0, v.acao)
                v = v.pai
            return caminho
        if v.estado not in x:
            x.add(v.estado)
            for z in expande(v):
                f.put(z)
    return None


def menor_custo(fila, hamming):
    menorNo = fila[0]
    for elemento in fila:
        if(hamming):
            if(elemento.custo_total_hamming < menorNo.custo_total_hamming):
                menorNo = elemento
        else:
            if(elemento.custo_total_manhattan < menorNo.custo_total_manhattan):
                menorNo = elemento
    return menorNo


def astar(estado, hamming):
    objetivo = "12345678_"
    caminho = []
    x = set()
    f = []
    f.append(Nodo(estado, None, None, 0))
    f[0].calcula_custo_total()
    while (f != []):
        v = menor_custo(f, hamming)
        f.remove(v)
        if v.estado == objetivo:
            while v.pai is not None:
                caminho.insert(0, v.acao)
                v = v.pai
            return caminho
        if v.estado not in x:
            x.add(v.estado)
            for z in expande(v):
                if z.estado not in x:
                    z.calcula_custo_total()
                    f.append(z)
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
    return astar(estado, True)


def astar_manhattan(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    return astar(estado, False)


if __name__ == "__main__":
    # print(custo_hamming("2_3541687"))
    start_time = time.time()
    a = dfs("2_3541687")
    print(time.time() - start_time)

    start_time = time.time()
    b = bfs("2_3541687")
    print(time.time() - start_time)
    # print(custo_manhattan("2_3541687"))
    start_time = time.time()
    c = astar_hamming("2_3541687")
    print(time.time() - start_time)
    # print(len(p))

    start_time = time.time()
    d = astar_manhattan("2_3541687")
    print(time.time() - start_time)
    # print(len(q))
