class Pet:
    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso
        self.fome = 0
        self.sede = 0

    def get_nome(self):
        return self.nome
    
    def get_peso(self):
        return self.peso
    
    def get_fome(self):
        return self.fome
    
    def get_sede(self):
        return self.sede
    
    #os sets

    def set_nome(self, nome_novo):
        self.nome = nome_novo
    
    def set_peso(self, novo_peso):
        self.peso = novo_peso

    def set_fome(self, novo_fome):
        self.fome = novo_fome
    
    def set_sede(self, nova_sede):
        self.sede = nova_sede

    def imprimir(self):
        print(f'Meu nome eh {self.nome}')
        print(f'Peso {self.peso}')
        print(f'Estou com {self.fome} fome')
        print(f'E de sede {self.sede}')

caozinho = Pet('Marie', 15)
caozinho.set_fome(10)
caozinho.set_sede(5)
caozinho.imprimir()