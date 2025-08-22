import random

n = random.choice([5, 5])
print(f"numero sorteado {n}")

matriz = [[0 for _ in range(n)] for _ in range(n)]
matriz_custo = [[0 for _ in range(n)] for _ in range(n)]

# Completa matriz adjacência com 1 e 0
for i in range(n):
    for j in range(i, n):
        valor = random.choice([0, 1])
        if i == j:
            valor = 0

        matriz[i][j] = valor
        matriz[j][i] = valor

# printa a matriz
print("\nMatriz de Adjacência:")
for linha in matriz:
    print(linha)

# completa aleatoriamente a matriz custo com os pesos de cada aresta
for i in range(n):
    for j in range(i, n):
        valor = random.randint(1, 5)
        if matriz[i][j] == 1:  # posições onde existe aresta
            matriz_custo[i][j] = valor
            matriz_custo[j][i] = valor
        elif matriz[i][j] == 0:  # posições onde não existe aresta
            matriz_custo[i][j] = 1000
            matriz_custo[j][i] = 1000

print("\nMatriz de Custos:")
for linha in matriz_custo:
    print(linha)


# -------------------------------
# Implementação do Dijkstra sem heapq
# -------------------------------
def dijkstra(matriz_custo, inicio):
    n = len(matriz_custo)
    dist = [1000] * n        # custo mínimo até cada nó
    dist[inicio] = 0
    visitado = [False] * n   # nós já processados

    for _ in range(n):
        # 1. Encontrar o nó não visitado com menor distância
        min_dist = 1000
        u = -1
        for i in range(n):
            if not visitado[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i

        if u == -1:  # não há mais nós alcançáveis
            break

        # 2. Marcar como visitado
        visitado[u] = True

        # 3. Atualizar distâncias dos vizinhos
        for v in range(n):
            if not visitado[v] and matriz_custo[u][v] != 1000:
                if dist[u] + matriz_custo[u][v] < dist[v]:
                    dist[v] = dist[u] + matriz_custo[u][v]

    return dist


# Entrada do usuário
inicio = int(input("\nDigite em qual vértice deseja começar (1 a n): ")) - 1
distancias = dijkstra(matriz_custo, inicio)

print(f"\nCusto mínimo partindo do vértice {inicio+1}:")
for i, d in enumerate(distancias):
    print(f" - Até o vértice {i+1}: {d}")
