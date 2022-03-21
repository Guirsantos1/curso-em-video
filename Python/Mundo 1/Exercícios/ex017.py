from math import hypot
co = float(input('Digite o número do cateto oposto: '))
ca = float(input('Digite o número do cateto adjancente: '))
'''hip = (co ** 2 + ca ** 2) **(1/2)'''
hip = hypot (co, ca)
print (
    f'O valor da hipotenusa é {hip:.2f}'
)
