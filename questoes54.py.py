cont_leve_baixa = 0
cont_pesado_alto = 0

for i in range(1, 8):
    print(f"--- {i}ª PESSOA ---")
    peso = float(input("Digite o peso (Kg): "))
    altura = float(input("Digite a altura (m): "))

    # Acumulando altura para a média
    soma_altura += altura

    # b) Quantas pessoas pesam mais de 90Kg
    if peso > 90:
        cont_90kg += 1

    # c) Pessoas com menos de 50Kg e menos de 1.60m
    if peso < 50 and altura < 1.60:
        cont_leve_baixa += 1

    # d) Pessoas com mais de 1.90m e mais de 100Kg
    if altura > 1.90 and peso > 100:
        cont_pesado_alto += 1

# Cálculo da média de altura
media_altura = soma_altura / 7

print("-" * 40)
print(f"a) A média de altura do grupo é: {media_altura:.2f}m")
print(f"b) Pessoas com mais de 90Kg: {cont_90kg}")
print(f"c) Pessoas com menos de 50Kg e menos de 1.60m: {cont_leve_baixa}")
print(f"d) Pessoas com mais de 1.90m e mais de 100Kg: '{cont_pesado_alto}'")