valor_casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o seu salário mensal? R$ '))
anos = int(input('Em quantos anos pretende pagar? '))

meses = anos * 12
prestacao = valor_casa / meses
limite_salario = salario * 0.30

print('\n' + '='*30)
print(f'Para pagar uma casa de R$ {valor_casa:.2f} em {anos} anos,')
print(f'a prestação será de R$ {prestacao:.2f}.')
print('='*30)

if prestacao <= limite_salario:
    print('EMPRÉSTIMO CONCEDIDO!')
    print('A parcela compromete menos de 30% da sua renda.')
else:
    print('EMPRÉSTIMO NEGADO!')
    print(f'A parcela de R$ {prestacao:.2f} excede o seu limite de R$ {limite_salario:.2f} (30% do salário).')