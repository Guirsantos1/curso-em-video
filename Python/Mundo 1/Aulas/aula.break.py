'''n = cont = 0
while  n !=999: #Isso seria a flag (BANDEIRA DE PARADA PARA O PROGRAMA)
    n = int(input('Digite um número:' ))
    cont +=1
print('Acabou')'''

'''n = s = 0
while n !=999:
    n = int(input('Digite um número:' ))
    s += n
s -=999 #<-- ISSO É UMA GAMBIARRA PQ O PROGRAMA VAI SOMAR O 999. E DEPOIS SUBTRAIR
print(f'A soma vale {s}')'''

n = s = 0
while True:
    n = int(input('Digite um número:' ))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')