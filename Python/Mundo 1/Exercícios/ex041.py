import datetime
nasc = int(input('Ano de nascimento:'))
atual = datetime.date.today().year
idade = atual - nasc
if idade <= 9:
    print('MIRIM')
elif 9 < idade <= 14:
    print('INFANTIL')
elif 14 < idade <= 19:
    print('JUNIOR')
elif 19 < idade <= 25:
    print('SENIOR')
elif idade > 25:
    print('MASTER')
