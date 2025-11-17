class MaxHeap:
    def __init__(self):
        self.heap = [None] #posição 0 não será utilizada
        
    def parent(self, i):
        return i // 2
    
    def filho_esquerdo(self, i):
        return 2 * i #retorna o índice do filho esquerdo
    
    def filho_direito(self, i):
        return 2 * i + 1 #retorna o índice do filho direito
    
    def max_heapify(self, i): #corrige ordem de prioridade do heap
        tamanho_heap = len(self.heap) - 1 #tamanho do heap (desconsidera índice 0)
        esquerdo = self.filho_esquerdo(i) #índice do filho esquerdo
        direito = self.filho_direito(i) #índice do filho direito
        topo = i #inicializa topo como o índice atual

        #verifica se o filho esquerdo é maior que o topo
        if esquerdo <= tamanho_heap and self.heap[esquerdo]["idade"] > self.heap[topo]["idade"]:
            topo = esquerdo #atualiza topo se o filho esquerdo for maior

        #verifica se o filho direito é maior que o topo
        if direito <= tamanho_heap and self.heap[direito]["idade"] > self.heap[topo]["idade"]:
            topo = direito #atualiza topo se o filho direito for maior

        #se o indice do topo é diferente do índice atual, maior filho é maior do que o pai
        if topo != i:
            self.heap[i], self.heap[topo] = self.heap[topo], self.heap[i] #troca os valores
            self.max_heapify(topo) #chama automaticamente para o índice atualizado

    
    def insert(self, paciente): #insere um novo paciente no heap
        self.heap.append(paciente) #adiciona o novo paciente no final do heap
        i = len(self.heap) - 1 #índice do novo paciente

        # Sobe enquanto necessário
        while i > 1 and self.heap[self.parent(i)]["idade"] < self.heap[i]["idade"]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i] #troca o paciente com o pai
            i = self.parent(i) #atualiza o índice para o pai


    def maximum(self):
        if len(self.heap) <= 1:
            raise Exception("Heap vazio")
        return self.heap[1] #retorna o maior elemento do heap (raiz), não pode ser indice 0
    
    
    def extract_max(self): #remove o maior elemento
        if len(self.heap) <= 1:
            raise Exception("Heap vazio")

        maior = self.heap[1] #guarda o maior elemento (topo)
        self.heap[1] = self.heap[-1] #substitui o topo pelo último elemento
        self.heap.pop() #remove o último elemento
        self.max_heapify(1) #corrige a ordem do heap a partir do topo
        return maior #retorna o maior elemento removido


    def increase_key(self, i, nova_idade): #aumenta o valor de um elemento no heap
        if nova_idade < self.heap[i]["idade"]:
            raise Exception("Novo valor é menor que o valor atual")
        
        self.heap[i]["idade"] = nova_idade #atualiza o valor do elemento

        #enquanto o elemento não for a raiz e o pai for menor
        while i > 1 and self.heap[self.parent(i)]["idade"] < self.heap[i]["idade"]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i] #troca o elemento com o pai
            i = self.parent(i) #atualiza o índice para o pai    

    def __str__(self):
        return str(self.heap[1:]) #retorna a representação em string do heap (ignora índice 0)
