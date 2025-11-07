class No:
    def __init__(self, elemento):
        self.dado = elemento
        self.proximo = None
    
class PilhaEncadeada:
    def __init__(self):
        self.topo = None
        self.tamanho = 0

    def push(self, item): #Adiciona item ao topo da pilha
        novo_no = No(item)
        novo_no.proximo = self.topo
        self.topo = novo_no
        self.tamanho += 1

    def pop(self):
        if self.topo == None:
            raise Exception("Pilha vazia")
        dado_removido = self.topo.dado
        self.topo = self.topo.proximo
        self.tamanho -= 1
        return dado_removido
    
    def peek(self):
        if self.topo == None:
           raise Exception("Pilha vazia")
        return self.topo.dado

