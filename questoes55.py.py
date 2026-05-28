import random

acertou = False

print("--- JOGO DA ADIVINHAÇÃO ---")
print("Tente adivinhar o número que eu pensei entre 1 e 10.")
print("Você tem 4 tentativas!")

for tentativa in range(1, 5):
    palpite = int(input(f"Tentativa {tentativa}: Qual o seu palpite? "))

    if palpite == numero_sorteado:
        print(f"Parabéns! Você acertou o número '{numero_sorteado}'!")
        acertou = True
        break
    elif palpite < numero_sorteado:
        print("Mais... Tente um número maior.")
    else:
        print("Menos... Tente um número menor.")

if not acertou:
    print("-" * 30)
    print(f"Que pena! Suas tentativas acabaram. O número era '{numero_sorteado}'.")