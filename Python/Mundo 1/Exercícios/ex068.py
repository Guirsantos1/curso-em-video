from random import randint
v = 0 
while True:
    jogadorn = int(input('Diga o valor:' ))
    maquina = randint(0,10)
    total = jogadorn + maquina
    tipo = ' '
    while tipo not in 'pi':
        tipo = str(input('[P]ar / [I]mpar? ')).strip().lower()[0]
    print(f'Você jogou {jogadorn} dedos, Maquina jogou {maquina} dedos, total foi {total}')
    print('DEU PAR' if total %2 == 0 else 'DEU IMPAR')
    if tipo == 'p':
        if total %2 == 0:
            print('Você venceu')
            v +=1
        else:
            print('Você perdeu')
            break
    elif tipo == 1:
        if total %2 == 1:
            print(f'Você ganhou')
            v += 1
        else:
            print('Você Perdeu')
            break
    print('tente novamente')
print('Você ganhou {}')
