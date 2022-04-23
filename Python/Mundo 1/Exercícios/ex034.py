s = float(input('Salario do funcionario:R$ '))
n1 = s + (s * 15 / 100)
n2 = s + (s * 10 / 100)
if s <= 1.250:
    print(f'O salario de {s} reais será agora R${n1}!')
else:
    print(f'O salario de {s} reais será agora R${n2}!')
#corrigir           