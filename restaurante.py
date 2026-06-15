class Restaurante:
    restaurante = []

    def _init_(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.cardapio = []
        Restaurante.restaurantes.append(self)

alfredus = Restaurante('Alfredus', 'Pizzaria')
podra = Restaurante('podrao', 'Hamburgueria')
mcdonalds = Restaurante('mcdonalds', 'Plastico')


def _str_(self):
       return f'{self.nome} | {self.categoria}'
    
alfredus = Restaurante('Alfredus', 'Pizzaria')
 
print(alfredus)


