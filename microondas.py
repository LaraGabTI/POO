class Microondas:
    def __init__(self,):
        self.painel = False
        self.botao = False
        self.tempo = 0

    def get_tempo(self):
        return self.tempo
    
    def get_botao(self):
        return self.botao
    
    def set_tempo(self, novo_tempo):
        if self.painel == True:
            self.tempo = novo_tempo

        else:
            print('desligado')

    def botao_on(self):
        if self.tempo > 0: 
            self.botao = True 
            print('Aquecendo...')
        else:
            print('Determine o tempo')

    def ligar(self):
        self.painel = True
        print('O Microondas está ligado')

    def desligar(self):
        self.painel = False
        print('O Microondas está desligado')

microondas = Microondas()
microondas.ligar()
microondas.set_tempo(30)
microondas.botao_on()
microondas.desligar()