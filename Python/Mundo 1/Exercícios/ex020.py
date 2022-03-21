from random import sample
n1 = str(input('Digite o nome do 1° aluno: '))
n2 = str(input('Nome do 2° aluno '))
n3 = str(input('Nome do 3° aluno '))
n4 = str(input('Nome do 4° aluno '))
lista = sample([n1,n2,n3,n4],k=4)
print( 'A ordem dos alunos é: '
)
print (
    f'{lista}'
)
