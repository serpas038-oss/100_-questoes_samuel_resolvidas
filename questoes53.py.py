soma_idade_grupo = 0
soma_idade_homens = 0
total_homens = 0
total_mulheres = 0
mulheres_mais_20 = 0

for i in range(1, 6):
    print(f"--- {i}ª PESSOA ---")
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").strip().upper()

    soma_idade_grupo += idade

    if sexo == 'M':
        total_homens += 1
        soma_idade_homens += idade
    elif sexo == 'F':
        total_mulheres += 1
        if idade > 20:
            mulheres_mais_20 += 1

# Cálculos de média
media_grupo = soma_idade_grupo / 5
media_homens = soma_idade_homens / total_homens if total_homens > 0 else 0

print("-" * 30)
print(f"a) Homens cadastrados: {total_homens}")
print(f"b) Mulheres cadastradas: {total_mulheres}")
print(f"c) Média de idade do grupo: {media_grupo:.1f}")
print(f"d) Média de idade dos homens: {media_homens:.1f}")
print(f"e) Mulheres com mais de 20 anos: '{mulheres_mais_20}'")