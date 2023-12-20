class Pet:
    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso
        self.fome = 0
        self.sede = 0
        self.comida = 100

    # Os GETS:
    def get_nome(self):
        return self.nome
    
    def get_peso(self):
        return self.peso
    
    def get_fome(self):
        return self.fome
    
    def get_sede(self):
        return self.sede
    
    # Os SETS:

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def set_peso(self, novo_peso):
        self.peso = novo_peso

    def set_fome(self, novo_fome):
        self.fome += novo_fome
        if self.fome >= 99:
            print(f'Alimente o {self.nome}')
            nova_comida = int(input('Quanto de comida quer dar pro seu pet? '))
            self.comida -= nova_comida
            self.fome -= nova_comida    
    
    def set_sede(self, novo_sede):
        self.sede = novo_sede

    def imprimir(self):
        print(f'Olá, me chamo {self.nome}')
        print(f'Estou pesando {self.peso}kg')
        print(f'Minha fome está em {self.fome}')
        print(f'Minha sede está em {self.sede}')

caozinho = Pet('Bodó', 15)
caozinho.imprimir()
caozinho.set_fome(20)
caozinho.imprimir()
caozinho.set_fome(30)
caozinho.imprimir()
caozinho.set_fome(70)
caozinho.imprimir()