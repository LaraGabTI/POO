class Pessoa: #super classe
    def __init__(self, nome, idade): #atributos em comum de prof e aluno
        self.nome = nome
        self.idade = idade
        self.__cpf = None
    
    def get_cpf(self):
        return self.__cpf
    
    def set_cpf(self, meu_cpf):
        self.__cpf = meu_cpf

class Professor(Pessoa): #classe filho
    def __init__(self, nome, idade, salario, disciplina, cpf): #atributos 
        super().__init__(nome, idade) #recebe da classe super
        self.salario = salario
        self.disciplina = disciplina
        self.cpf = super().set_cpf(cpf) #recebe da classe super
    
    def __str__(self):  #funcao que imprime tudo
        return f'Nome: { self.nome }, Idade: { self.idade } e CPF: { self.get_cpf() } Salario: { self.salario }, Disciplina: { self.disciplina }.'
    
class Aluno(Pessoa):
    pass

paulo = Professor('Paulo Junior', 29, 1400.00, 'Backend', 1234567890)

print(paulo) #chamado assim por conta da funcao string