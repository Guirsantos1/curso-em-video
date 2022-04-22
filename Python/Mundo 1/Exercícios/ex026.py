frase = str(input('Digite alguma frase:')).strip().upper()
print(('Na frase digitada a letra A é repetida') , frase.count('A')  , 'vezes')
print(('A primeira letra A aparece na posição:') , frase.find('A')+1)
print(('A ultima letra A aparece na posição:') , frase.rfind('A')+1)