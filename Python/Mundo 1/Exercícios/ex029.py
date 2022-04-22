velcar = int(input('Sua velocidade atual é de :'))
if velcar > 80:
    print('Sua velocidade é superior a 80km/h, você foi multado!')
    print(f'E sua multa será de R$ {(velcar - 80) * 7}')
else:
    print('Sua velocidade está dentro do permitido, siga uma boa viagem!')
