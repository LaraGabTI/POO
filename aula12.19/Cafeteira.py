class Cafeteira:
    def __init__(self):
        self.cafe = False
        self.ligada = False
        self.compartimento_agua = False

    def ligar(self):
        self.ligada = True
    
    def desligar(self):
        self.ligada = False

    def verificar_agua(self):
        if self.ligada == True:
            if self.compartimento_agua == False:
                print('Coloque a agua')
            else:
                self.compartimento_agua = True