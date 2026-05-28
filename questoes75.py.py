vetor = [1, 1]

for i in range(2, 16):
    proximo_numero = vetor[i - 1] + vetor[i - 2]
    vetor.append(proximo_numero)

for valor in vetor:
    print(valor, end=" ")
print() 

for indice in range(len(vetor)):
    print(f"'{indice}'", end=" ")
print() 