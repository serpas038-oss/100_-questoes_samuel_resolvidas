soma = 0
contagem = 1

print("Iniciando leitura...")

while contagem <= 7:
    num = int(input(f"Digite o {contagem}º valor: "))
    soma += num
    contagem += 1

print(f"O somatório entre os números digitados é: '{soma}'")