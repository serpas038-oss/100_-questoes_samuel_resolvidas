Inicializa os vetores para nomes e idades
nomes = []
idades = []

for i in range(1, 10):
    nome = input(f"Digite o nome da {i}ª pessoa: ")
    idade = int(input(f"Digite a idade de {nome}: "))
    
    nomes.append(nome)
    idades.append(idade)

print("-" * 50)
print("Listagem de pessoas menores de idade:")
print("-" * 50)

algum_menor = False
for i in range(9):
    if idades[i] < 18:
        
        print(f"Nome: '{nomes[i]}' - Idade: '{idades[i]}'")
        algum_menor = True

if not algum_menor:
    print("Nenhuma pessoa menor de idade foi cadastrada.")