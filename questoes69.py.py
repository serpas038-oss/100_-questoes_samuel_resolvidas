print("--- GERADOR DE PA ---")


primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))

soma = 0
termo_atual = primeiro

print("Sequência: ", end="")


for i in range(1, 11):
    print(termo_atual, end=" -> " if i < 10 else " ")
    soma += termo_atual
    termo_atual += razao

print("\n" + "-" * 20)
print(f"A soma de todos os valores é: '{soma}'")