vetor_nomes = []

for i in range(7):
    nome = input(f"Digite o {i+1}º nome: ")
    vetor_nomes.append(nome)

print("\n--- Listagem na Ordem Inversa ---")

vetor_invertido = vetor_nomes[::-1]

    print(f"'{nome}'", end=" ")
print() 

for indice in range(len(vetor_invertido)):
    print(f"'{indice}'", end=" ")
print() 