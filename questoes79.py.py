vetor = []

for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))
    vetor.append(num)

print("\n--- Números Pares e suas Posições ---")

for indice in range(len(vetor)):
    
    if vetor[indice] % 2 == 0:
        
        print(f"Número: '{vetor[indice]}' na Posição: '{indice}'")