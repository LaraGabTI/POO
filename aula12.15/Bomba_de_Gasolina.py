class BombaGasolina:
    def __init__(self, qnttCombustivel):
        self.qnttCombustivel = qnttCombustivel
        self.tipoCombustivel = None
        self.valorLitro_alcool = 2.20
        self.valorLitro_gas = 3.90
        self.valorPagar = 0

    def get_qtdd_Combustivel(self):
        return self.qnttCombustivel
    
    def set_qtdd_Combustivel(self, nova_qtdd):
        self.qnttCombustivel = self.nova_qtdd
    
    def get_valores(self):
        print(f'O valor da gasolina eh {self.valorLitro_gas}')
        print(f'O valor da alcool eh {self.valorLitro_alcool}')

    def escolha(self, tipoCombustivel):
        self.tipoCombustivel = input("Digite A para Alcool e G para gasolina")
        if self.tipoCombustivel == 'A':
            Alcool()
        elif self.tipoCombustivel == 'G':
            Gasolina()
        else:
            print("Não temos esse combustivel")
    
class Alcool(BombaGasolina):
    def __init__(self, qtdd_Combustivel):
        super().__init__(qtdd_Combustivel)
        
           
    def get_valorLitro_gas(self):
        return self.valorLitro_gas

    def set_valorLitro_gas(self, novo_valor_gas):
        self.valorLitro_gas = self.novo_valor_gas
    
    def valorPago(self, valorLitro, qnttCombustivel):
        return self.qnttCombustivel * valorLitro
        

class Gasolina(BombaGasolina):
        #
    
    '''def get_valorLitro_alcool(self):
        return self.valorLitro_alcool
    def set_valorLitro_alcool(self, novo_valor_alcool):
        self.valorLitro_alcool = self.novo_valor_alcool  '''
    pass


