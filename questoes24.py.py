distancia = float(input("Qual a distância da viagem em Km? "))

if distancia <= 200:
    preco_km = 0.50
else:
    preco_km = 0.45

total = distancia * preco_km

print(f"Para uma viagem de {distancia}Km, a taxa é de R${preco_km:.2f} por Km.")
print(f"O preço total da passagem será: R${total:.2f}")