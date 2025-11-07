#Um entregador de app precisa levar pedidos por uma cidade representado por uma grade NxM
#Cada célula do mapa tem um custo de esforço, uma ladeira(custo alto), andar no palno(baixo)
#O entregador só pode se mover para direita e para baixo, além de que não pode voltar
#O objetivo é saber qual o caminho que gastará o menor esforço para ele chegar do início
#(canto superior esquerdo) até o destino(canto inferir direito)

def entregador(C):
    n = len(C)      #linhas
    m = len(C[0])   #colunas

    F = [[0 for _ in range(m)] for _ in range(n)]

    F[0][0] = C[0][0]

    for j in range(1, m):
        F[0][j] = C[0][j] + F[0][j-1] #Preenche primeira linha

    for i in range(1, n):
        F[i][0] = C[i][0] + F[i-1][0] #Prenche a primeira coluna

    for i in range(1, n):
        for j in range(1, m):
            F[i][j] = C[i][j] + min(F[i-1][j], F[i][j-1])

    return F[n-1][m-1] #Essa subtração é para ajustar a diferença, pois a contagem começa do 0

C = [
    [1, 3, 1, 2],
    [2, 1, 8, 1],
    [4, 2, 1, 3],
    [1, 1, 8, 1]
]

resultado = entregador(C)
print("Menor esforço total:", resultado)