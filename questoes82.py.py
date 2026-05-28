notas = []

for i in range(1, 11):
    nota = float(input(f"Digite a nota do aluno {i}: "))
    notas.append(nota)

media = sum(notas) / len(notas)

maior_nota = max(notas)

alunos_acima_media = sum(1 for nota in notas if nota > media)

posicoes = [f"'{index + 1}'" for index, nota in enumerate(notas) if nota == maior_nota]

print("-" * 40)
print(f"a) Média da turma: {media:.2f}")
print(f"b) Quantos alunos estão acima da média: {alunos_acima_media}")
print(f"c) Qual foi a maior nota digitada: {maior_nota:.2f}")
print(f"d) Posições onde a maior nota aparece: {' '.join(posicoes)}")