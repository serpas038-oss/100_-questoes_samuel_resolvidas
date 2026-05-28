salario_atual = float(input('Digite o salário atual: R$ '))
genero = input('Qual o gênero (M/F)? ').upper().strip()
anos_empresa = int(input('Há quantos anos trabalha na empresa? '))

if genero == 'F':
    if anos_empresa < 15:
        aumento = 5
    elif 15 <= anos_empresa <= 20:
        aumento = 12
    else:
        aumento = 23

elif genero == 'M':
    if anos_empresa < 20:
        aumento = 3
    elif 20 <= anos_empresa <= 30:
        aumento = 13
    else:
        aumento = 25

else:
    aumento = 0
    print('\n"Gênero não identificado. Nenhum ajuste aplicado."')

if aumento > 0:
    novo_salario = salario_atual + (salario_atual * aumento / 100)
    print('\n' + '-'*35)
    print(f'Gênero: "{genero}"')
    print(f'Tempo de casa: "{anos_empresa} anos"')
    print(f'Aumento aplicado: "{aumento}%"')
    print(f'Novo salário: "R$ {novo_salario:.2f}"')
    print('-'*35)