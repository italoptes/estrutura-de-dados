class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaSimplismenteEncadeada:
    def __init__(self):
        self.cabeca = None
        self.cauda= None
        self.atual = None
        self.contador = 0

    def is_vazia(self):
        if self.contador == 0:
            return True

    def adiciona_no_comeco(self, elemento):
        novo_no = No(elemento)
        if self.is_vazia():
            self.cabeca =  novo_no
            self.cauda = novo_no
        else:
            novo_no.proximo = self.cabeca
            self.cabeca = novo_no
        self.contador += 1
        self.atual = self.cabeca

    def adiciona_no_final(self, elemento):
        novo_no = No(elemento)
        if self.is_vazia():
            self.cabeca =  novo_no
            self.cauda = novo_no
        else:
            self.cauda.proximo = novo_no
            self.cauda = novo_no
        self.contador += 1

    def remover_inicio(self):
        if self.is_vazia():
           raise Exception("A lista está vazia, não é possível remover do início!")
        dado_removido = self.cabeca.dado
        self.cabeca = self.cabeca.proximo
        self.contador -= 1
        if self.is_vazia():
            self.cauda = None
        self.atual = self.cabeca
        return dado_removido
    
    def remover_final(self):
        if self.is_vazia():
           raise Exception("A lista está vazia, não é possível remover do início!")
        dado_removido = None
        if self.cabeca ==  self.cauda:
            dado_removido = self.cabeca.dado
            self.cabeca = None
            self.cauda = None
            self.atual = None
        else:
            no_anterior = self.cabeca
            while no_anterior.proximo != self.cauda:
                no_anterior = no_anterior.proximo
            dado_removido = self.cauda.dado
            no_anterior.proximo = None
            self.cauda = no_anterior
            self.atual = self.cabeca
        self.contador -= 1
        return dado_removido

    def buscar(self, elemento):
        atual = self.cabeca
        while atual:
            if atual.valor == elemento:
                return atual
            atual = atual.proximo
        return None
    
    