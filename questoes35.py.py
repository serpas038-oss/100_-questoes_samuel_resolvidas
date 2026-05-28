print('Categorias: [1] Carro Popular | [2] Carro de Luxo')
tipo = int(input('Escolha o tipo de carro (1 ou 2): '))
dias = int(input('Quantos dias de aluguel? '))
km = float(input('Quantos Km foram percorridos? '))

if tipo == 1:
    diaria = 90
    if km <= 100:
        taxa_km = 0.20
    else:
        taxa_km = 0.10
    total = (dias * diaria) + (km * taxa_km)
    print(f'\nCategoria: "Carro Popular"')

elif tipo == 2:
    diaria = 150
    if km <= 200:
        taxa_km = 0.30
    else:
        taxa_km = 0.25
    total = (dias * diaria) + (km * taxa_km)
    print(f'\nCategoria: "Carro de Luxo"')

else:
    total = 0
    print('\n"Opção inválida!"')

if total > 0:
    print(f'Total de dias: "{dias}"')
    print(f'Km percorridos: "{km}"')
    print(f'Valor total a pagar: "R$ {total:.2f}"')