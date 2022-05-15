from random import randint
lista = ('Pedra','Papel','Tesoura')
maquina = randint (0,2)
print('''Suas Opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual sua jogada ? '))
print(f'O Computador jogou: {lista[maquina]}') #lista e maquina juntos para pegar da lista com o random da maquina.
print(f'O Jogador jogou: {lista[jogador]}')
if jogador == maquina:
    print('EMPATE')
#MAQUINA JOGA PEDRA
elif maquina == 0:
    if jogador == 1:
        print('VOCÊ GANHOU')
    elif jogador == 2:
        print('VOCÊ PERDEU')
    else:
        print('Jogada invalida')
#MAQUINA JOGA PAPEL
elif maquina == 1:
    if jogador == 0:
        print('VOCÊ PERDEU')
    elif jogador == 2: 
        print('VOCÊ GANHOU')
    else:
        print('Jogada invalida')
#MAQUINA JOGA TESOURA        
elif maquina == 2:
    if jogador == 0:
        print('VOCÊ GANHOU')
    elif jogador == 1:
        print('VOCÊ PERDEU')
    else:
        print('Jogada invalida')
