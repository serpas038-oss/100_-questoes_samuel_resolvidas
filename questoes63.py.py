somatorio = 0
total_valores = 0
menor_valor = None
quantidade_pares = 0

print("--- ANALISADOR DE NÚMEROS ---")

while True:
    numero = int(input("Digite um valor: "))
    
    # a) Somatório
    somatorio += numero
    total_valores += 1
    
    # b) Menor valor (Lógica de inicialização)
    if menor_valor is None or numero < menor_valor:
        menor_valor = numero
        
    # d) Quantidade de pares
    if numero % 2 == 0:
        quantidade_pares += 1
        
    # Pergunta de continuidade (Condição do Enquanto)
    continuar = input("Quer continuar? [S/N]: ").strip().upper()
    print("-" * 30)
    
    if continuar == 'N':
        break

# c) Cálculo da média
media = somatorio / total_valores if total_valores > 0 else 0

print(f"a) O somatório entre todos os valores é: {somatorio}")
print(f"b) O menor valor digitado foi: {menor_valor}")
print(f"c) A média entre todos os valores é: {media:.2f}")
print(f"d) Quantos valores são pares: '{quantidade_pares}'")