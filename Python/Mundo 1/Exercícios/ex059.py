n1 = float(input('Primeiro valor: '))
n2 = float(input('segundo valor: '))
user = 0
while user !=6:
    user = int(input('''
    [1] SOMAR
    [2] MULTIPLICAR
    [3] DIVIDIR
    [4] MAIOR
    [5] NOVO VALOR
    [6] SAIR
    Escolha sua opção: '''))
    if user == 1:
        print(n1 + n2)
    elif user == 2:
        print(f'{n1 * n2:.2f}')
    elif user == 3:
        print(f'Os valores {n1} e {n2} dividios são: {n1 / n2:.2f}')
    elif user == 4:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1:.2f} e {n2:.2f} o maior valor é {maior:.2f}')
    elif user == 5:
        print('informe os numeros novamente')
        n1 = float(input('Primeiro valor: '))
        n2 = float(input('Segundo valor: '))
print('Fim do programa. Volte sempre 😁')
    
