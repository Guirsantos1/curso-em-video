ano = int(input('Digite um ano: '))
dezena = ((ano % 100))
ano1 = ano%400
ano2 = dezena%4
if dezena == 0:
    if ano1 == 0:
        print('ele é bissexto')
    else:
        print('não é bissexto')
else:
    if ano2 == 0:
        print('ele é bissexto')
    else:
        print('Ele não é bissexto!')