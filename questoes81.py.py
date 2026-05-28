vetor_idades = []

for i in range(8):
    idade = int(input(f"Digite a idade da {i+1}ª pessoa: "))
    vetor_idades.append(idade)


soma_idades = sum(vetor_idades)
media_idade = soma_idades / len(vetor_idades)

maior_idade = max(vetor_idades)

print("\n--- RESULTADOS ---")

for idade in vetor_idades:
    print(f"'{idade}'", end=" ")
print()

print("Posições (índices):", end=" ")
for indice in range(len(vetor_idades)):
    print(f"'{indice}'", end=" ")
print("\n" + "-"*18)

print(f"a) Média de idade: '{media_idade:.1f}' anos")

print("b) Posições com mais de 25 anos:", end=" ")
maiores_25 = False
for indice in range(len(vetor_idades)):
    if vetor_idades[indice] > 25:
        print(f"'{indice}'", end=" ")
        maiores_25 = True
if not maiores_25:
    print("'Nenhuma'", end=" ")
print()

print(f"c) Maior idade digitada: '{maior_idade}' anos")

print("d) Posições onde foi digitada a maior idade:", end=" ")
for indice in range(len(vetor_idades)):
    if vetor_idades[indice] == maior_idade:
        print(f"'{indice}'", end=" ")
print()