# crie abstração para uma super classe funcionario com duas subclasses. Imprima todos do dados.

class Funcionarios:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = 0.0
    
    def get_nome(self):
        return self.nome 
    
    def get_salario(self):
        return self.salario
    
    
    
class Gerente(Funcionarios):
    def __init(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def __str__(self):  #funcao que imprime tudo
        return f'Nome: { self.nome }, Idade: { self.idade } e Salario: { self.salario }.'

class Desenvolvedor(Funcionarios):
    def __init(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def __str__(self):  #funcao que imprime tudo
        return f'Nome: { self.nome }, Idade: { self.idade } e Salario: { self.salario }.'
    