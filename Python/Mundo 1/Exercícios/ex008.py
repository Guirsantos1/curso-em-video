metros = float(input ('Digite o valor em metros:'))
cm = metros * 100 
mm = metros * 1000
km = metros / 100
print ('Seu valor {:.1f} Metros\nEm Kilometros é {:.1f}km\nEm centimetros é:{:.1f}cm\nEm milímetros é:{:.1f}mm\n \n'.format(metros, km, cm, mm))