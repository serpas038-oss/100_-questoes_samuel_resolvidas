def Gerador(mensagem, quantidade):

    linha_visual = "+-------=======------+"
    
    
    print(f"'{linha_visual}'")
    
    
    for _ in range(quantidade):
        print(f"'{mensagem}'")
        
    
    print(f"'{linha_visual}'")


Gerador("Aprendendo Portugol", 4)