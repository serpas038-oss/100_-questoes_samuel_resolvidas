nomes = []
sexos = []
salarios = []

for i in range(1, 6):
    nome = input(f"Digite o nome do {i}º funcionário: ")
    # .strip().upper() remove espaços e padroniza para maiúsculo (M ou F)
    sexo = input(f"Digite o sexo de {nome} (M/F): ").strip().upper()
    salario = float(input(f"Digite o salário de {nome}: R$ "))
    
    nomes.append(nome)
    sexos.append(sexo)
    salarios.append(salario)

print("-" * 60)
print("Listagem: Funcionárias mulheres que ganham mais de R$ 5.000,00")
print("-" * 60)

encontrou_funcioneira = False
for i in range(5):
    if sexos[i] == 'F' and salarios[i] > 5000:
        
        print(f"Nome: '{nomes[i]}' - Sexo: '{sexos[i]}' - Salário: 'R$ {salarios[i]:.2f}'")
        encontrou_funcioneira = True

if not encontrou_funcioneira:
    print("Nenhuma funcionária atende aos critérios estabelecidos.")