nome = input("Digite o nome do cliente: ")
sexo = input("Digite o sexo [M/F]: ").upper().strip()
valor_compras = float(input("Qual o valor total das compras? R$ "))

# Definindo a porcentagem de desconto baseada no sexo
if sexo == "F":
    desconto = 13
    status = "Mulher"
elif sexo == "M":
    desconto = 5
    status = "Homem"
else:
    desconto = 0
    status = "Não identificado"

# Cálculos
valor_desconto = valor_compras * (desconto / 100)
preco_final = valor_compras - valor_desconto

# Exibição dos resultados
print("-" * 30)
print(f"Cliente: {nome}")
print(f"Categoria: {status}")
print(f"Desconto aplicado: {desconto}%")
print(f"Valor original: R$ {valor_compras:.2f}")
print(f"Preço final com desconto: R$ {preco_final:.2f}")
print("-" * 30)