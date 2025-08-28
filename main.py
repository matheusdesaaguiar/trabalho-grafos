import random

import networkx as nx
import matplotlib.pyplot as plt

n = random.choice([10,50,100]) #Sorteia o numero de vértices
print(f"numero sorteado {n}") 

#Cria duas matrizes quadradas com o tamanho sorteado
matrizadjacencia = [[0 for _ in range(n)] for _ in range(n)]
matrizcusto = [[0 for _ in range(n)] for _ in range(n)]

# Completa matriz de adjacência passando apenas por metade dela
for i in range(n):
    for j in range(i+1, n):  # evita diagonal e duplicação
        if random.random() < 0.02:  # 2% de chance de existir aresta
            matrizadjacencia[i][j] = 1
            matrizadjacencia[j][i] = 1

        else:
            matrizadjacencia[i][j] = 0
            matrizadjacencia[j][i] = 0

# Garante conexidade com uma cadeia 
for i in range(1, n):#passa por todos os vértices para ligar eles, garantido que ele tenha pelo menos uma ligação com o grafo
    j = random.randint(0, i-1)#sorteia um vértice menor que i para ligar o vértice atual
    matrizadjacencia[i][j] = 1 #insere um na matriz adjacencia
    matrizadjacencia[j][i] = 1 


#printa a matriz de adjacência
print("\nMatriz de Adjacência:")
for linha in matrizadjacencia:
    print(linha)

# Completa aleatoriamente a matriz de custos
for i in range(n):
    for j in range(i, n):
        if i == j:
            matrizcusto[i][j] = 0  # diagonal principal sempre tem 0
        elif matrizadjacencia[i][j] == 1:  # se exitir ligação entre os vértices da um custo aleatorio
            valor = random.randint(1, 5)
            matrizcusto[i][j] = valor
            matrizcusto[j][i] = valor  
        else:  # se não existir ligação coloca um numero alto 
            matrizcusto[i][j] = 1000
            matrizcusto[j][i] = 1000

#printa a matriz de custo
print("\nMatriz de Custos:")
for linha in matrizcusto:
    print(linha)

#Algoritimo de Dijkstra
def dijkstra(matrizcusto, origem):
    n = len(matrizcusto) #pega o numero de linhas da matriz para saber a quantidade de vértices

    melhorCaminho = [1000] * n   # vetor que vai guardar a menor distancia da origem para cada vértice todos começão como infinito
    melhorCaminho[origem] = 0    # a posição de origem não tera custo por isso 0
    verticesVisitados = [False] * n   # vetor para saber quais vértices foram visitados

    for _ in range(n):
        # Encontra o vértice não visitado com menor distância
        menorDist = 1000
        verticeAtual = -1
        for i in range(n): #vai percorrer todos os vértices
            if not verticesVisitados[i] and melhorCaminho[i] < menorDist: #verifica se o vértice i ainda não foi visitado e se a distancia até ele é a menor
                menorDist = melhorCaminho[i] #paga a distancia para o vértice i 
                verticeAtual = i #define o vértice i como o atual para testar as distancias partindo dele 

        if verticeAtual == -1:  # se o vértice for -1 significa que todos ja foram visitados
            break

        # Marca o vértice atual como visitado
        verticesVisitados[verticeAtual] = True

        # Relaxa as arestas vizinhas
        for vizinho in range(n): # for para verificar os vizinhos do vértice atual e atualizar os custos
            if not verticesVisitados[vizinho]: # so servem vértices que não foram vizitados 
                novaDist = melhorCaminho[verticeAtual] + matrizcusto[verticeAtual][vizinho] # Calcula a distância total para chegar ao vizinho passando pelo vértice atual
                if novaDist < melhorCaminho[vizinho]: # compara a distancia calculada com a que ja esta no vetor para saber qual a melhor
                    melhorCaminho[vizinho] = novaDist #se for melhor guarda no vetor 

    return melhorCaminho #retorna o vetor com os melhores caminhos

# Exemplo: origem = 0
origem = 0
resultado = dijkstra(matrizcusto, origem)

print(f"\nMenores caminhos a partir do vértice {origem}:")
print(resultado)

#####################################################
################### Desenha Grafo ###################
#####################################################
# Cria grafo
G = nx.Graph()
for i in range(n):
    G.add_node(i)
for i in range(n):
    for j in range(i+1, n):
        if matrizadjacencia[i][j] == 1:
            G.add_edge(i, j, weight=matrizcusto[i][j])

# Função para recuperar o caminho mínimo de Dijkstra 
def recuperar_caminho(matrizcusto, origem, destino, melhorCaminho):
    n = len(matrizcusto)
    caminho = [destino]
    atual = destino
    while atual != origem:
        for vizinho in range(n):
            if matrizadjacencia[atual][vizinho] == 1:
                if melhorCaminho[atual] == melhorCaminho[vizinho] + matrizcusto[vizinho][atual]:
                    caminho.append(vizinho)
                    atual = vizinho
                    break
    caminho.reverse()
    return caminho

# Cria lista de arestas do caminho mínimo
arestas_caminho = []
for destino in range(n):
    if destino != origem:
        caminho = recuperar_caminho(matrizcusto, origem, destino, resultado)
        for i in range(len(caminho)-1):
            arestas_caminho.append((caminho[i], caminho[i+1]))

# Posições dos nós
pos = nx.spring_layout(G)

# Desenha nós
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700, font_size=10)

# Desenha todas as arestas em cinza
nx.draw_networkx_edges(G, pos, width=1, edge_color='gray')

# Desenha as arestas do caminho mínimo em vermelho
nx.draw_networkx_edges(G, pos, edgelist=arestas_caminho, width=2, edge_color='red')

# Mostra os pesos
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.show()