#Dado um tabuleiro de tamanho NxM, em que cada casa dele há no maximo uma moeda
#Existe um robô que só pode se mover para direita e para baixo, além de que ele não volta!
#Qual o número máximo de moedas que pode ser coletadas por esse robô
#O robô termina o trajeto no canto inferior direito do tabuleiro

def coletor(C):
    # C é o tabuleiro original, onde cada posição C[i][j] indica se há moeda (1) ou não (0)
    # F é uma matriz auxiliar que guarda o maior número de moedas que o robô pode coletar até cada casa

    n = len(C)      #linhas
    m = len(C[0])   #colunas

    F = [[0 for _ in range(m)] for _ in range(n)] #Cria a matriz F cheia de zeros(mesmo tamanho de C)
    #Essa matriz vai sendo preenchida ao decorrer dos casos

    F[0][0] = C[0][0]   #Caso base: primeira e mais simplificada opção

    for j in range(1, m):    #Preenche a primeira linha, iniciando do 1 até m
        F[0][j] = C[0][j] + F[0][j-1]
    
    for i in range(1, n):   #Preenche a primeira coluna, iniciando do 1 até n
        F[i][0] = C[i][0] + F[i-1][0]

    for i in range(1, n):    #Preenche o restante da matriz
        for j in range(1, m):
            F[i][j] = C[i][j] + max(F[i-1][j], F[i][j-1])
            #C[i][j]: moeda atual
            #max(...): escolhe o melhor caminho (de cima ou da esquerda)
            #F[i][j]: total máximo de moedas coletadas até essa posição

    return F[n-1][m-1]   #Retorna o total máximo de moedas coletadas até o canto inferior direito

C = [
    [1, 0, 1],
    [1, 0, 1],
    [1, 0, 1]
]

resultado = coletor(C)
print("Máximo de moedas coletadas:", resultado)