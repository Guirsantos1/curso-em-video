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
    if sexo == 'F' and idade >20:
            contmulher +=1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar ?' )).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total de pessoas com mais de 18 anos: {cont18}')
print(f'O total de homens cadastrado foi {conthomem}')
print(f'O total de mulher com mais de 20 anos: {contmulher}')