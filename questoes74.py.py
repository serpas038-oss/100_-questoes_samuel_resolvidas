vetor = []

for i in range(10):
    if i % 2 == 0:
        vetor.append(5)  
    else:
        vetor.append(3)  
for valor in vetor:
    print(valor, end=" ")
print() 

for indice in range(len(vetor)):
    print(f"'{indice}'", end=" ")
print() 