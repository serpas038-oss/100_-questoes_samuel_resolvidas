print("--- OS 10 PRIMEIROS TERMOS DE FIBONACCI ---")

t1 = 1
t2 = 1

print(f"{t1} {t2}", end=" ")

for i in range(3, 11):
    proximo = t1 + t2
    print(proximo, end=" ")
    
    t1 = t2
    t2 = proximo

print("\n" + "-" * 40)
print("'Acabou!'")