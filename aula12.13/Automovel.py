class Automovel:

    def __init__ (self, placa, cor): #init construtor do atributo
        self.placa = placa #privado
        self.cor = cor

    def get_placa(self): #metodo
        return self.placa
        
    def dirigir(self, velocidade): #metodo
        print(f'Estou dirigindo a {velocidade}km/h')
    
    def get_cor(self):
        return self.cor 
    
    def set_cor(self, nova_cor): #alterar o atributo 
        self.cor = nova_cor

carro = Automovel('VSF', 'rosa') #carro é uma instancia de automovel
print(carro.get_placa())
carro.dirigir(220)
print(carro.get_cor())
carro.set_cor('vermelho')
#print(carro.get_cor())
carro.get_cor = 'amarelo'
moto = Automovel('Uou', 'preto')
print(moto.get_placa())

