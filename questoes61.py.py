contador = 0

print("--- CONTAGEM PROGRESSIVA ---")

# Simulando a estrutura "Faça... Enquanto"
while True:
    print(contador, end=" ")
    
    # Incremento de 3 em 3
    contador += 3
    
    # Condição de parada (Enquanto contador for menor ou igual a 30)
    if contador > 30:
        break

print("'Acabou!'")