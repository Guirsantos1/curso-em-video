casa = float(input('Valor da casa: '))
sal = float(input('Renda do comprador: '))
ano = int(input('Anos de financiamento: '))
parcela = casa / ano / 12
libera = sal / 100 * 30
if parcela <= libera:
    print(f'O valor da casa em {ano} anos a prestação será de R${parcela:.2f} Emprestimo LIBERADO !')
else: 
    print(f'O valor da casa em {ano} anos a prestação será de R${parcela:.2f} Emprestimo NEGADO !')