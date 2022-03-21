from math import ceil, sqrt
num = int(input('Digite um número: '))
raiz =  sqrt (num)
print ('A raiz do numero {} é igual a {:.2f}'.format(num, ceil(raiz)))
