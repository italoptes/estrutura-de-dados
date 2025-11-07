class Pilha:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.dados = [None] * capacidade
        self.topo = -1

    def resize(self):
        nova_capacidade = self.capacidade * 2 
        novos_dados = [None] * nova_capacidade
        for i in range(self.topo + 1):
            novos_dados[i] = self.dados[i]
        self.dados = novos_dados
        self.capacidade = nova_capacidade

    def is_empyt(self):
        return self.topo == -1;

    def push(self, elemento):
        if self.topo == self.capacidade - 1:
            self.resize(self)
        self.topo += 1
        self.dados[self.topo] = elemento

    def pop(self):
        if self.is_empyt:
            raise Exception("Pilha vazia")
        dado_retorno = self.dados[self.topo]
        self.topo -= 1
        return dado_retorno
    
    def peek(self):
        if self.is_empyt(self):
            raise Exception("Pilha vazia")
        return self.dados[self.topo]

