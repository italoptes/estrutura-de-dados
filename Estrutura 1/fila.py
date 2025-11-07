class Fila:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.dados = [None] * capacidade
        self.cabeca = 0
        self.cauda = -1
        self.tamanho = 0

    def enqueue(self, elemento):
        if self.tamanho == self.capacidade:
            raise Exception("Fila cheia")
        else:
            self.dados[self.cauda] = elemento
            self.cauda +=1 
            self.tamanho +=1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Fila vazia")
        else:
            dado = self.dados[self.cabeca]
            self.cabeca = self.cabeca + 1
            self.tamanho -= 1
            return dado
        
    def peek(self):
        if self.is_empty():
            raise Exception("Fila vazia")
        else:
            return self.dados[self.cabeca]
        
    def is_empty(self):
        if self.tamanho == 0:
            return True
        
    