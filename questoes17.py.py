velocidade = float(input('Qual é a velocidade atual do carro? '))

if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido de 80km/h.')
    multa = (velocidade - 80) * 5
    print(f'O valor da multa é de R${multa:.2f}!')

print('Tenha um bom dia! Dirija com segurança.')