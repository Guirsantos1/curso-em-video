r1 = float(input('Escreva a primeira reta: '))
r2 = float(input('Escreva a segunda reta: '))
r3 = float(input('Escreva a terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Estas retas podem criar um triangulo:')
else:
    print('Essas retas não formam um triangulo: ')
