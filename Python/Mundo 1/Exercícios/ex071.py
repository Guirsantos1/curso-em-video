print(25*'-')
print('Caixa Eletrônico')
print(25*'-')
valor = int(input('Qual valor deseja sacar ? ')) 
total = valor
nota = 50
cont = 0
while True:
    if total >= nota:
        total -= nota   
        cont += 1
    else:
        print(f'O total de {cont} notas de R${nota} !')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        cont = 0
        if total == 0:
            break
print('Obrigado !')