from heap import MaxHeap

hospital = MaxHeap()

# Adicionando pacientes
hospital.insert({"nome": "Maria", "idade": 82})
hospital.insert({"nome": "João", "idade": 40})
hospital.insert({"nome": "Ana", "idade": 65})
hospital.insert({"nome": "Pedro", "idade": 12})
hospital.insert({"nome": "Clara", "idade": 90})

print("Fila de prioridade (heap):")
print(hospital)

# Quem tem maior prioridade?
print("\nPaciente com maior prioridade agora:")
print(hospital.maximum())

# Chamando o próximo paciente
print("\nChamando paciente para atendimento...")
print(hospital.extract_max())

print("\nFila após chamamento:")
print(hospital)

# Aumentando prioridade
print("\nAumentando prioridade do João (índice 1) para 95 anos...")
hospital.increase_key(1, 95)

print("\nFila atualizada:")
print(hospital)
