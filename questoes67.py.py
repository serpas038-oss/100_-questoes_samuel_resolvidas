print("--- CONTADOR PERSONALIZADO ---")


valor = int(input("Digite um valor inteiro positivo: "))

print("Contagem: ", end="")


for i in range(0, valor + 1):
    
    if i < valor:
        print(i, end=", ")
    else:
        print(i, end=", ")

print("'FIM!'")