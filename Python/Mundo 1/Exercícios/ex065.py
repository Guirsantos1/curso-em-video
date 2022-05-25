resp = 'S'
soma = cont = media = maior = menor = 0
while resp == 'S':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n 
    resp = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
media = soma / cont
print(f'Você digitou {cont} números, a média foi {media:.2f}')
print(f'O maior valor foi {maior} e o menor valor foi {menor}')
