print('-=' * 15)
print('   GERADOR DE PA')
print('-=' * 15)
primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Qual é a razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais !=0:
    total = total + mais
    while cont <=total:
        print(termo, end = ' → ')
        termo += razão
        cont +=1
    mais = int(input('PAUSA\nQuantos termos você quer mostras a mais? '))
print(f'Progressão finalizada. {cont} PA exibidas !')
