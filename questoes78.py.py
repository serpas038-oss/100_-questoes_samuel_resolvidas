vetor = []

for i in range(15):
    num = int(input(f"Digite o {i+1}º número: "))
    vetor.append(num)

print("\n--- Vetor Completo ---")

for valor in vetor:
    print(f"'{valor}'", end=" ")
print()

for indice in range(len(vetor)):
    print(f"'{indice}'", end=" ")
print("\n")

print("--- Posições dos Múltiplos de 10 ---")

for indice in range(len(vetor)):
    if vetor[indice] % 10 == 0:
        print(f"'{indice}'", end=" ")
print()