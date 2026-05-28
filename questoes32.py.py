import random
from time import sleep

def main():
    print('-=' * 20)
    print("Vou pensar em um número entre 1 e 5. Tente adivinhar!")
    print('-=' * 20)
    
    
    numero_secreto = random.randint(1, 5) 
    
    try:
        
        palpite = int(input('Em que número eu pensei? '))
        
        print('\nProcessando...')
        sleep(1.5) 
        
        
        if palpite == numero_secreto:
            
            print(f'PARABÉNS! Você acertou! Eu realmente pensei no número '{numero_secreto}'.")
        else:
            print(f'GANHEI! Eu pensei no número \'{numero_secreto}' e não no '{palpite}'.')
            
    except ValueError:
        print('Erro: Por favor, digite apenas números inteiros.')

if __name__ == '__main__':
    main()