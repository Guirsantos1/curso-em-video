maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f'{c}° Peso(Kg): '))
    if peso > maior:
        maior = peso
    if menor == 0 or peso < menor:
        menor = peso
print(f'Maior Peso foi {maior}Kg \nMenor peso foi {menor}Kg')