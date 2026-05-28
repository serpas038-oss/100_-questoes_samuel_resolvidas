from datetime import date

ano_atual = date.today().year

nascimento = int(input("Em que ano você nasceu? "))
idade = ano_atual - nascimento

print(f"Quem nasceu em {nascimento} tem {idade} anos em {ano_atual}.")

if idade < 18:
    saldo = 18 - idade
    ano_alistamento = ano_atual + saldo
    print(f"Ainda faltam {saldo} anos para o seu alistamento.")
    print(f"Seu alistamento será em {ano_alistamento}.")
elif idade > 18:
    saldo = idade - 18
    ano_alistamento = ano_atual - saldo
    print(f"Você já deveria ter se alistado há {saldo} anos.")
    print(f"Seu alistamento foi em {ano_alistamento}.")
else:
    print("Você deve se alistar IMEDIATAMENTE este ano!")