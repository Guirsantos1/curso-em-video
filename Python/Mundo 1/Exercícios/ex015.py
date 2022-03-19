dias = float(input('Quantos dias o carro foi alugado?'))
km = float(input('Quantos KM foi percorrido?'))
vd = dias * 60
vkm = km * 0.15  
total = vd + vkm
print ('O valor em dias:R${:.2f}\nO valor em KM:R${:.2f}\nO valor total:R${:.2f}'.format(vd, vkm, total))