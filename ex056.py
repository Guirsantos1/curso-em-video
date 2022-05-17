somaidade = 0
mediaidade = 0
maioridade = 0
nomevelho = 0
menoridade = 0
for p in range (1,5):
    print(f'----- {p}° Pessoa -----')
    nome = str(input(f'Nome: ')).strip()
    idade = int(input(f'Idade: '))
    sexo = str(input(f'Sexo (M/F): ')).strip()
    somaidade += idade
    mediaidade = somaidade / 4
    if p == 1 and sexo in 'Mn':
        maioridade = idade
        nomevelho = nome
    if sexo in 'Mm' and idade >maioridade:
        maioridade = idade
        nomevelho = nome
    if sexo in 'Ff' and idade <20:
        menoridade +=1 
print(f'Media total de idade: {mediaidade}!')
print(f'Homem com maior idade: {nomevelho}!')
print(f'Quantidade de mulheres com menos de 20 anos: {menoridade}!')
