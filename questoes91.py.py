def Maior(n1, n2):
    if n1 > n2:
        print('O maior valor e:', n1)
    elif n2 > n1:
        print('O maior valor e:', n2)
    else:
        print('Os dois valores sao iguais.')

valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))

Maior(valor1, valor2)