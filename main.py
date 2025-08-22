import random

n = random.choice([5,5])
print(f"numero sorteado {n}")

matriz = [[0 for _ in range(n)] for _ in range(n)]
matrizcusto = [[0 for _ in range(n)] for _ in range(n)]

#Completa matriz adjacencia com 1 e 0
for i in range(n):
    for j in range(i,n):
        valor = random.choice([0,1])
        if i == j:
            valor=0

        matriz[i][j] = valor
        matriz[j][i] = valor

#printa a matriz
for linha in matriz:
    print(linha)

#completa aleatoriamente a matriz custo com os pesos de cada aresta
for i in range(n):
    for j in range(i,n):
        valor = random.randint(1,5)
        if matriz[i][j] == 1:  #posições onde existe aresta
            matrizcusto[i][j] = valor
            matrizcusto[j][i] = valor
        elif matriz[i][j] == 0: #posições onde não existe aresta
            matrizcusto[i][j] = 1000
            matrizcusto[j][i] = 1000
    
print(f"\n")

for linha in matrizcusto:
    print(linha)

print(f"\n")

# comentario para dar commit 