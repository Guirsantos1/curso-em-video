from random import randint
computador = randint (0,5)
print('Pensei em um número entre 0 e 5')
jogador = int(input('Qual numero foi que pensei ? '))
if jogador == computador:
    print(f'PARABÉNS, você ganhou, eu pensei no numero {computador} !')
else:
    print(f'VOCÊ PERDEU.\nEu pensei no numero {computador} e vc digitou o numero {jogador} !')