horas_atividade = float(input('Quantas horas de atividade física você fez no mês? '))

if horas_atividade <= 10:
    pontos_por_hora = 2
elif horas_atividade <= 20:
    pontos_por_hora = 5
else:
    pontos_por_hora = 10

total_pontos = horas_atividade * pontos_por_hora
faturamento = total_pontos * 0.05

print('\n' + '='*30)
print(f'Horas registradas: "{horas_atividade}h"')
print(f'Pontos acumulados: "{total_pontos} pontos"')
print(f'Valor a receber: "R$ {faturamento:.2f}"')
print('='*30)