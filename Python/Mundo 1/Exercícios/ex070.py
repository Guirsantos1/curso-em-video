print(20*'-')
print(4*' ','LOJAS GUI')
print(20*'-')
soma = prodmil = cont = menor =  0
barato = ' '
while True:
    prod = str(input('Nome do produto:' )).strip().title()
    prec = float(input('Preço: '))
    soma += prec
    cont += 1
    if cont == 1 or prec < menor:
        menor = prec
        barato = prod
    if prec > 1000:
        prodmil +=1
    resp = ' '
    while resp not in 'SN': #Pode ser tbm while resp !='S' and resp != 'N'
        resp = str(input('Quer continuar comprando [S/N]? ' )).strip().upper()[0]
    if resp == 'N':
        break
print(10*'-','FIM DO PROGRAMA',10*'-')
print(f'O total da compra foi R${soma:.2f}\n{prodmil} Produtos com valor acima de R$1000.00')
print(f'O produto mais barato foi {barato} no valor de R$ {menor}')