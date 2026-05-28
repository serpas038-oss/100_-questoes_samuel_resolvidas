idades = []
cont_18 = 0
cont_5 = 0

for i in range(1, 11):
    idade = int(input(f"Digite a idade da {i}ª pessoa: "))
    idades.append(idade)
    
    if idade > 18:
        cont_18 += 1
    if idade < 5:
        cont_5 += 1

media = sum(idades) / len(idades)
maior_idade = max(idades)

print("-" * 30)
print(f"a) Média de idade: {media:.1f}")
print(f"b) Mais de 18 anos: {cont_18}")
print(f"c) Menos de 5 anos: {cont_5}")
print(f"d) Maior idade lida: '{maior_idade}'")