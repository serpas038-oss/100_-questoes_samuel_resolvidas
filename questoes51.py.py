maior_preco = 0
menor_preco = 0

for i in range(1, 9):
    preco = float(input(f"   Digite o preço do {i}º produto: R$"'))
    
        if i == 1:
        maior_preco = preco
        menor_preco = preco
    else:
        
        if preco > maior_preco:
            maior_preco = preco
        
        
        if preco < menor_preco:
            menor_preco = preco

print("-" * 30)
print(f"O maior preço digitado foi: 'R$ {maior_preco:.2f}"')
print(f"O menor preço digitado foi: 'R$ {menor_preco:.2f}"')