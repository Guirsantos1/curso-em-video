from datetime import date
n = int(input('Data do nascimento '))
idade = date.today().year - n 
if idade == 18:
    print('Voce deve se alistar o quanto antes !')
elif idade < 18:
    print('Voce ainda não precisa se alistar !')
elif idade >= 19:
    print('Voce passou do prazo de alistamento !')
