nome = 'Paulo'
print(nome.isalpha()) #letras
print(nome.isdigit()) #numero
print('')

nome = 'paulo22'
print(nome.isalpha()) 
print(nome.isdigit())
print('')

n = '1'
print(n.isalpha()) 
print(n.isdigit())
print('')


numero = input('Digite um numero:')
if numero.isdigit() == True:
    print('Ok é numero')