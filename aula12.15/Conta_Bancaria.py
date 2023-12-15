class ContaBancaria:
    def __init__(self, num_conta, titular,):
        self.num_conta = num_conta
        self.titular = 'titular'
        self.saldo = 0
        self.deposito = []
        self.saque = []

    def verifica(self):
        if type(self.num_conta) == int:
            if self.titular.isalpha() == True:
                return True
            else: 
                print("Titular aceita apenas letras")
        else:
            print("Numero da conta aceita apenas inteiro")
        
    def get_saldo(self):
        if self.verifica():
            return self.saldo

    def get_deposito(self):
        self.verifica()
        return self.deposito
    
    def get_saque(self):
        if self.verifica():
            return self.saque
    
    def set_deposito(self, deposito):
        if self.verifica():
            self.saldo += deposito
            self.deposito.append(deposito)
            return self.deposito
    
    def set_saque(self, saque):
        if self.verifica():
            if self.saldo <= 0:
                print("O valor do seu saldo eh 0, operação negada")
            elif saque <= self.saldo:
                print(f'Saque de {saque} reais realizado com suceso')
                self.saldo -= saque
                self.saque.append(saque)
                return saque
            else:
                print(f'Voce esta com o saldo zerado, operação negada')
            

    
    def extrato_Conta(self):
        print(f'Numero da sua conta eh {self.num_conta}')
        print(f'Seu saldo eh {self.saldo}')
        print(f'Seu deposito foi de {self.deposito}')
        print(f'Seu saque foi de {self.saque}')



Titular1 = ContaBancaria(1234, 'Lara')
Titular1.set_deposito(200)
Titular1.set_saque(10)
Titular1.set_deposito(5)
Titular1.set_saque(300)
Titular1.extrato_Conta()

    

