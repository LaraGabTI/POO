class CaixaRegistradora:
    def __init__(self, total_da_compra, qtdd_recebida):
        self.fundo_caixa = 100.00
        self.total_da_compra = total_da_compra
        self.status = False
        self.qtdd_recebida = qtdd_recebida


    
    def get_total_compra(self):
        return self.total_da_compra
    
    def set_total_compra(self, novo_total):
        if self.abrir_caixa == True:
            self.total_da_compra = novo_total
            print(f'voce gastou {self.total_da_compra}')
        else:
            print('Caixa fechado')
    
    def get_qtdd_recebida(self):
        return self.qtdd_recebida
    
    def set_qtdd_recebida(self, novo_qtdd_recebida):
        if self.abrir_caixa == True:
            self.qtdd_recebida = novo_qtdd_recebida
            print(f'voce pagou {self.qtdd_recebida}')
        else:
            print('Caixa fechado')
        
    
    def abrir_caixa(self):
        self.status = True
        return f'Caixa aberto'

    def fechar_caixa(self):
        self.status = False
        return f'Caixa fechado'

    def caixa(self):
        if self.status == True:
            self.fundo_caixa += self.total_da_compra
            return f'caixa eh {self.fundo_caixa}'
        else:
            return 'Caixa fechado'
    
    def troco(self):
        if self.status == True:
            return f'seu troco {self.qtdd_recebida - self.total_da_compra}' 
        else: 
            return 'Caixa fechado'
    
compra1 = CaixaRegistradora(300, 400)
print(compra1.abrir_caixa())
print(compra1.troco())
print(compra1.caixa())
print('')
compra1.set_total_compra(200)
compra1.set_qtdd_recebida(400)
print(compra1.troco())
print(compra1.caixa())
print(compra1.fechar_caixa())

#compra2 = 