class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class FilaEncadeada:
    def __init__(self):
        self.cabeca = None
        self.cauda = None
        self.tamanho = 0

    def enqueue(self, intem): #Adiciona elemento
        novo_no = No(intem)
        if self.cabeca == None: #Se a lista estiver vazia
            self.cabeca =  novo_no
            self.cauda =  novo_no
        else:
            self.cauda.proximo = novo_no # O antigo fim aponta para o novo nó
            self.cauda =  novo_no        # O novo nó se torna o fim  
        self.tamanho += 1

    def dequeue(self):
        if self.cabeca == None:
            raise Exception("Fila vazia")
        valor_removido = self.cabeca.dado
        self.cabeca = self.cabeca.proximo
        self.tamanho -= 1
        if self.cabeca is None: # Se a fila ficou vazia após a remoção
            self.fim = None     # O fim também deve ser None
        return valor_removido


    