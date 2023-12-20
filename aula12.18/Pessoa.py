class Pessoa: #super classe
    def __init__(self, nome, idade): #atributos em comum de prof e aluno
        self.nome = nome
        self.idade = idade
        self.__cpf = None #cpf privado
    
    def get_cpf(self):
        return self.__cpf
    
    def set_cpf(self, meu_cpf):
        self.__cpf = meu_cpf #privado

class Professor(Pessoa): #classe filho
    def __init__(self, nome, idade, salario, disciplina, cpf): #atributos 
        super().__init__(nome, idade) #recebe da classe super, n consegue o privado
        self.salario = salario
        self.disciplina = disciplina
        self.cpf = super().set_cpf(cpf) #recebe da classe super
    
    def __str__(self):  #funcao que imprime tudo
        return f'Nome: { self.nome }, Idade: { self.idade } e CPF: { self.get_cpf() } Salario: { self.salario }, Disciplina: { self.disciplina }.'
    
class Aluno(Pessoa):
    def __init__(self, nome, idade, cpf):
        super().__init__(nome, idade)        
        self.cpf = super().set_cpf(cpf)
        self.notasGeral = 0

    def notas(self, n1, n2, n3, n4):
        self.notasGeral = ((n1 + n2 + n3 + n4) / 4)
    
    def get_notas(self):
        return self.notasGeral
  
    def __str__(self):  #funcao que imprime tudo
        return f'Nome: { self.nome }, Idade: { self.idade } e CPF: { self.get_cpf() } notas Getal: { self.notasGeral} .'

paulo = Professor('Paulo Junior', 29, 1400.00, 'Backend', 1234567890)
lara = Professor('Lara', 22, 1500, 'Matematica', 8252918360)
print(paulo) #chamado assim por conta da funcao string
print(lara)

paula = Aluno('Paula', 22, 828282)
paula.notas(8, 9, 10, 5)
print(paula)