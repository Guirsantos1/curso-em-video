maior = 0
menor = 0
for p in range (1,6):
    peso = float(input(f'Peso da {p}° pessoa: '))
    if peso == 1:
         maior = p
         menor = p
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso 
print(f'O maior peso é {maior}Kg')
print(f'O menor peso é {menor}Kg')  
 