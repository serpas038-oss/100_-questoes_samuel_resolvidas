import random

vetor = [random.randint(0, 99) for _ in range(20)]

vetor_com_aspas = [f"'{num}'" for num in vetor]

print("Números gerados:")
print(" ".join(vetor_com_aspas))
print("-" * 60)

vetor.sort()

vetor_ordenado_com_aspas = [f"'{num}'" for num in vetor]

print("Valores ordenados em ordem crescente:")
print(" ".join(vetor_ordenado_com_aspas))