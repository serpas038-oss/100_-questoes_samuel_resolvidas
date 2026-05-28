import random

for _ in range(30):
    vetor.append(random.randint(1, 15))

print("--- Vetor Sorteado ---")
for valor in vetor:
    print(f"'{valor}'", end=" ")
print("\n")

chave = int(input("Digite um número (chave) entre 1 e 15 para buscar: "))

posicoes_encontradas = []
contador = 0

for indice in range(len(vetor)):
    if vetor[indice] == chave:
        posicoes_encontradas.append(indice)
        contador += 1

print("\n--- Resultado da Busca ---")

if contador > 0:
    print(f"A chave '{chave}' foi sorteada '{contador}' vezes.")
    print("Ela foi encontrada nas posições:", end=" ")
    for pos in posicoes_encontradas:
        print(f"'{pos}'", end=" ")
    print()
else:
    print(f"A chave '{chave}' não foi sorteada em nenhuma posição.")
