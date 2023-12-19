# crie abstração para uma super classe funcionario com duas subclasses. Imprima todos do dados.

class Funcionarios:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        self.ponto = False
    
    def get_nome(self):
        return self.nome 
    
    def get_salario(self):
        return self.salario
    
    def bater_ponto_entrada(self):
        self.ponto = True
        return f'Bateu o ponto pra entrar'
    
    def bater_ponto_saida(self):
        self.ponto = False
        return f'Bateu o ponto pra sair'
    
class Gerente(Funcionarios):
    def __init__(self, nome, salario, idade):
        super().__init__(nome, salario)
        self.idade = idade
        
    def __str__(self):  #funcao que imprime tudo
        return f'Nome: { self.nome }, Idade: { self.idade } e Salario: { self.salario }.'

class Desenvolvedor(Funcionarios):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def __str__(self):  #funcao que imprime tudo
        return f'Nome: { self.nome }, Idade: { self.idade } e Salario: { self.salario }.'
    
paulo = Gerente('Paulo', 1200, 22)
print(paulo)
print(paulo.bater_ponto_entrada())
