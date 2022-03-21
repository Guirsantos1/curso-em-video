from random import choice
print(
    f'Sorteio quem ira lavar louça'
)
n1 = str(input('Digite o primeiro nome : '))
n2 = str(input('Segundo nome: ' ))
n3 = str(input('Terceiro nome: ' ))
n4 = str(input('Quarto nome: ')) 
lista = [n1,n2,n3,n4]
r = choice(lista)
print (
    f'Quem ira lavar louça: {r}'
)