def Media(n1, n2):
    return (n1 + n2) / 2

def Situacao(m):
    if m >= 7.0:
        return 'APROVADO'
    elif 5.0 <= m < 7.0:
        return 'EM RECUPERACAO'
    else:
        return 'REPROVADO'

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media_final = Media(nota1, nota2)

status_aluno = Situacao(media_final)

print('Media obtida:', media_final)
print('Situacao do aluno:', status_aluno)