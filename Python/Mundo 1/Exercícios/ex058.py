from random import randint
maquina = randint (0,10)
print('Pensei em um número entre 0 e 10.')
print('Tente acertar!')
palpites = 0
jogador = 0
while jogador != maquina:
    jogador = int(input('Qual sua respota?  '))
    palpites +=1
print(f'''Parabéns o numero pensado foi {maquina}, !
Você acertou após {palpites} tentativas''')
