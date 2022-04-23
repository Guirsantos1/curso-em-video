d = float(input('Distancia da viagem em KM: '))
if d <= 200:
    print(f'A distancia de {d}KM\n ira custar R$ {d*0.50}')
else:
    print(f'A distancia de {d}KM\n ira custar R$ {d*0.45:.2f}')