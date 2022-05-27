print(20*'-')
print(5*' ','CADASTRO')
print(20*'-')
cont18 = conthomem = contmulher = 0
while True:
    idade = int(input('Sua idade: ' ))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo ([M]asc/[F]em): ')).strip().upper()[0]
    if idade >=18:
            cont18 +=1
    if sexo == 'M':
            conthomem += 1
    if idade >20 and sexo == 'F':
            contmulher +=1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar ?[S]im/[N]ão ' )).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total de pessoas maiores de idade: {cont18}')
print(f'{conthomem} Homens cadastrados')
print(f'Com {contmulher} Mulheres com mais de 20 anos:' )