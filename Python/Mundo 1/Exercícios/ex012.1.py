p = float(input('Digite o valor do protudo: R$'))
d = p - (p * 5 / 100)
print('O produto que custava R${:.2f} na promoção de 5% de desconto será:R${:.2f}'.format(p, d))
