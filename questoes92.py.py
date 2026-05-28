def ParOuImpar(num):
    if num % 2 == 0:
        print('O numero inserido e PAR.')
    else:
        print('O numero inserido e IMPAR.')

numero = int(input('Digite um numero inteiro: '))

ParOuImpar(numero)