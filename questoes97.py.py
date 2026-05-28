def Maior(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2 >= n1 and n2 >= n3:
        return n2
    else:
        return n3

v1 = float(input('Digite o primeiro valor: '))
v2 = float(input('Digite o segundo valor: '))
v3 = float(input('Digite o terceiro valor: '))

o_maior = Maior(v1, v2, v3)

print('O maior valor entre eles e:', o_maior)