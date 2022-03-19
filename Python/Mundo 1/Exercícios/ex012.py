p =float(input('Coloque aqui o valor do produto: '))
desc = 5 / 100
prod = p * desc
print('O valor de desconto de 5% é:R${:.2f}' .format(p * desc))
print('O valor do produto com desconto éR${:.2f}:'.format(p - prod))