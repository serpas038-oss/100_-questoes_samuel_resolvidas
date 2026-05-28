import random

# Listas e contadores
sorteados = []
acima_de_cinco = 0
divisiveis_por_tres = 0

# Sorteio de 20 números entre 0 e 10
for _ in range(20):
    num = random.randint(0, 10)
    sorteados.append(num)
    
    # b) Verifica se está acima de 5
    if num > 5:
        acima_de_cinco += 1
        
    # c) Verifica se é divisível por 3 (e não é zero)
    if num % 3 == 0 and num != 0:
        divisiveis_por_tres += 1

# Exibição dos resultados
print(f"a) Números sorteados: {sorteados}")
print(f"b) Quantos números estão acima de 5: '{acima_de_cinco}'")
print(f"c) Quantos números são divisíveis por 3: '{divisiveis_por_tres}'")