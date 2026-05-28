soma = 0
contagem = 1

print("Iniciando leitura...")

# Laço para ler 7 números
while contagem <= 7:
    num = int(input(f"Digite o {contagem}º valor: "))
    soma += num
    contagem += 1

# Exibição do resultado com uma aspas
print(f"O somatório entre os números digitados é: '{soma}'")