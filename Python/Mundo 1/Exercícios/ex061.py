print('-=' * 15)
print('   10 TERMOS DE UM P.A')
print('-=' * 15)
primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Qual é a razão da P.A: '))
termo = primeiro
cont = 1
while cont <=10:
    print(termo, end = ' → ')
    termo += razão
    cont +=1
print('ACABOU')