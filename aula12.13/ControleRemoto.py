class ControleRemoto:

    def __init__(self, cor, marca, qtdd_pilhas): 
        self.botao = None
        self.cor = cor
        self.marca = marca
        self.qtd_pilhas = qtdd_pilhas
        self.painel =  False
        self.temperatura = 0

    def ligar(self):
        self.painel = True
    
    def desligar(self):
        self.painel = False

    def set_temperatura(self, nova_temperatura):
        if self.painel == False :
            print('Temperatura não pode ser alterada, ar desligado')
        else: 
            self.temperatura = nova_temperatura

    def get_temperatura(self):
        return self.temperatura
    
    def pressionar_botao(self, tipo_de_botao):
        self.botao = tipo_de_botao
        if self.botao == 'Ligar' and self.temperatura == 0:
            print('Ar esta ligado')
            self.ligar()
        elif self.botao == 'Desliga':
            print('Ar esta desligado')
            self.set_temperatura(0)
            self.desligar()

controle = ControleRemoto('Rosa', 'elgin', 2)

controle.pressionar_botao('Desligar')
controle.pressionar_botao('Ligar')
controle.set_temperatura(20)
print(controle.get_temperatura())
controle.pressionar_botao('Desligar')
    

             
        