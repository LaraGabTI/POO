def __init (self, placa = 'XYZ-4925'): #init construtor do atributo
    self.placa = placa

    def get_placa(self): #metodo
        return self.placa
    
    def dirigir(delf, velocidade): #metodo
        print(f'Estou dirigindo a {velocidade}km/h')