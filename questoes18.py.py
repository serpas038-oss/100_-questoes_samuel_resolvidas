from datetime import date

atual = date.today().year
nascimento = int(input('Em que ano você nasceu? '))
idade = atual - nascimento

print(f'Quem nasceu em {nascimento} tem {idade} anos em {atual}.')

if idade < 16:
    print('Você ainda não pode votar.')
elif 16 <= idade < 18 or idade >= 70:
    print('Seu voto é opcional.')
else:
    print('Seu voto é obrigatório.')