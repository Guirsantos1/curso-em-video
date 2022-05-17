from datetime import date
hj = date.today().year
tmaior = 0
tmenor = 0 
for c in range (1,8):
    nasc = int(input(f'{c}° Data de nascimento: '))
    idade = hj - nasc
    if idade <= 18:
        tmaior += 1
    else:
        tmenor += 1
print(f' O total de maiores de idade é {tmaior}')
print(f' O total de menores de idade é {tmenor}')
