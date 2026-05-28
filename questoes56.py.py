soma = 0
numero = 0

print("--- SOMADOR DE NÚMEROS ---")
print("Digite os números que deseja somar.")
print("Para parar e ver o resultado, digite 1111.")
print("-" * 30)

while True:
    numero = int(input("Digite um número: "))
    
    
    if numero == 1111:
        break
        
    soma += numero

print("-" * 30)
print(f"O somatório de todos os valores digitados foi: '{soma}'")