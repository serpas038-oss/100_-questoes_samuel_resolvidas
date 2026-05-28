nome = input('Digite o nome do funcionário: ')
salario_atual = float(input(f'Digite o salário de {nome}: R$ '))
anos_empresa = float(input(f'Quantos anos {nome} trabalha na empresa? '))

if anos_empresa < 3:
    percentual = 3
elif 3 <= anos_empresa < 10:
    percentual = 12.5
else:
    percentual = 20

aumento = salario_atual * (percentual / 100)
novo_salario = salario_atual + aumento

print('-' * 30)
print(f'Funcionário: {nome}')
print(f'Tempo de casa: {anos_empresa} anos')
print(f'Percentual de aumento: {percentual}%')
print(f'Valor do aumento: R$ {aumento:.2f}')
print(f'Novo salário: R$ {novo_salario:.2f}')
print('-' * 30)