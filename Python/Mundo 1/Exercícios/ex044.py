print('>' * 10, 'Loja GUILHERME', '<' * 10)
valor = float(input('Digite o Valor Total das Compras: R$ '))
print('''Escolha a Forma de Pagamento:
 [1] à Vista ou no Cheque 
 [2] à Vista no Cartão 
 [3] 2x no Cartão 
 [4] 3x ou Mais no Cartão''''')
opcao = int(input('Qual é a opção ? '))
avista = (valor - valor * (10/100))
cartao = (valor - valor * (5/100))
parcelado = (valor + valor * (20/100))
print(f'O valor da sua compra foi R$ {valor:.2f}')
if(opcao == 1):
    print(f'Pagando a Vista, você ganha 10% de desconto, então o total a pagar é R$ {avista:.2f}')
elif(opcao == 2):
    print(f'Pagando a Vista no Cartão, você ganha 5% de desconto, então o total a pagar é R$ {cartao:.2f}')
elif(opcao == 3):
    print(f'Você pagará 2x de R$ {valor/2:.2f}')
elif(opcao == 4):
    vezes = int(input('Em quantas vezes? '))
    print(f'Sua compra será parcelada em {vezes}x de R$ {parcelado:.2f}')
    print(f'Sua compra de R$ {valor:.2f} terá um total de R$ {parcelado:.2f}')
else:
    print('Você não escolheu uma das Formas de Pagamento.')