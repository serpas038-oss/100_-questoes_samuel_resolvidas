print("--- GERADOR DE TABUADA ---")

num = int(input("Digite um valor para ver sua tabuada: "))

print(f"Tabuada do {num}:")
print("-" * 15)


for i in range(1, 11):
    resultado = num * i
    print(f"{num} x {i} = '{resultado}'")

print("-" * 15)