frase = input('Qual a frase? ').upper().replace(' ' , '')
print (f'{frase[::-1]}')
if frase == frase[::-1]:
    print('A frase é um palíndromo')
else:
    print('A frase não é um palíndromo')
