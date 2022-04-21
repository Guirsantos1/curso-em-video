n = input('Informe um numero:')
nf = f'{n:>4}'
print(f'Analisando o numero {n}')
print(f'Unidade: {nf[3]}')
print(f'Dezena: {nf[2]}')
print(f'centena:{nf[1]}')
print(f'milhar: {nf[0]}')