def Gerador(mensagem, quantidade, borda):
    estilos_borda = {
        1: "+-------=======------+",
        2: "~~~~~~~~:::::::~~~~~~~"
    }
    
    linha_visual = estilos_borda.get(borda, estilos_borda[1])
    
    print(f"'{linha_visual}'")
    
    for _ in range(quantidade):
        print(f"'{mensagem}'")
        
    print(f"'{linha_visual}'")


print("Exemplo com a Borda 1:")
Gerador("Aprendendo Portugol", 3, 1)

print("\nExemplo com a Borda 2:")
Gerador("Mudando o estilo em Python", 2, 2)