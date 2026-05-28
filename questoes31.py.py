import random
from time import sleep

def jogar():
    itens = ('Pedra', 'Papel', 'Tesoura')
    
    print('-' * 20)
    print('  JO KEN PO  ')
    print('-' * 20)
    print('[ 0 ] PEDRA')
    print('[ 1 ] PAPEL')
    print('[ 2 ] TESOURA')
    
    try:
        jogador = int(input('Qual é a sua jogada? '))
        if jogador not in [0, 1, 2]:
            print('Opção inválida! Escolha 0, 1 ou 2.')
            return

        computador = random.randint(0, 2)

        print('jo...')
        sleep(0.5)
        print('ken...')
        sleep(0.5)
        print('po!!!')
        sleep(0.5)

        print('-=' * 15)
        print(f'Computador jogou: {itens[computador]}')
        print(f'Jogador jogou: {itens[jogador]}')
        print('-=' * 15)

        
        if computador == jogador:
            print("EMPATE!")
        
        elif (jogador == 0 and computador == 2) or \
             (jogador == 1 and computador == 0) or \
             (jogador == 2 and computador == 1):
            print('JOGADOR VENCEU!')
            
        else:
            print('COMPUTADOR VENCEU!')

    ValueError:
        print('Erro: Por favor, digite apenas números.')

if __name__ == '__main__':
    jogar()