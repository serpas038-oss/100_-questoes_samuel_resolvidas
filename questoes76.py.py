import random

vetor = []

for _ in range(7):
    
    numero_aleatorio = random.randint(1, 100)
    vetor.append(numero_aleatorio)

for valor in vetor:
    print(f"'{valor}'", end=" ")
print() 

for indice in range(len(vetor)):
    print(f"'{indice}'", end=" ")
print() 