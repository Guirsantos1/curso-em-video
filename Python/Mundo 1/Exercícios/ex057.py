sexo = str(input('Digite seu sexo [M/F]:')).strip().upper() 
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos, repita o processo: ')).strip().upper()
print(f'Sexo {sexo} registrado !')
