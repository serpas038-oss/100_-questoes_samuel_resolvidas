total_idades = 0
soma_idades = 0
maiores_21 = 0

print("--- ANALISADOR DE IDADES ---")

while True:
    # O bloco "Faça" começa aqui
    idade = int(input("Digite a idade: "))
    
    total_idades += 1
    soma_idades += idade
    
    if idade >= 21:
        maiores_21 += 1
    
    # Pergunta para continuar (condição de interrupção)
    continuar = input("Deseja continuar? [S/N]: ").strip().upper()
    print("-" * 30)
    
    if continuar == 'N':
        break

# Cálculos finais
media = soma_idades / total_idades if total_idades > 0 else 0

print(f"a) Total de idades digitadas: {total_idades}")
print(f"b) Média das idades: {media:.1f}")
print(f"c) Pessoas com 21 anos ou mais: '{maiores_21}'")