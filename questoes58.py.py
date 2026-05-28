soma_idades = 0
total_alunos = 0

print("--- ANALISADOR DE TURMA ---")
print("Digite as idades dos alunos (ou 999 para encerrar).")

while True:
    idade = int(input("Idade: "))
    
    
    if idade == 999:
        break
        
    soma_idades += idade
    total_alunos += 1


if total_alunos > 0:
    media = soma_idades / total_alunos
    print("-" * 30)
    print(f"Total de alunos na turma: '{total_alunos}'")
    print(f"Média de idade do grupo: '{media:.1f}'")
else:
    print("Nenhum aluno foi cadastrado.")