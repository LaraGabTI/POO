class Televisao:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.canal = 0
        self.ligada = False

    def get_tamanho(self):
        return self.tamanho
    
    def get_canal(self):
        return self.canal
    
    def ligar(self):
        self.ligada = True
        return f'TV Ligada'
    
    def desligar(self):
        self.ligada = False
        return f'TV Desligada'

    def set_tamanho(self, novo_tamanho):
        self.tamanho = novo_tamanho
    
    def set_canal(self, trocar_canal):
        if trocar_canal < 0 or trocar_canal > 30:
            return f'Canal inexistente'
        else:
            if self.ligada == True:
                self.canal = trocar_canal
                return f'Canal foi trocado para o {self.canal}'
            else:
                return f'voce não pode trocar de canal, com a tv desligada'

    
    
tv1 = Televisao(36)
print(tv1.ligar())
print(tv1.set_canal(40))
