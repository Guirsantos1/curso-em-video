'''n = cont = soma = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]' ))
    soma += n
    cont +=1  
    if n == 999:
        n + n - n
print(f'Você digitou {cont-1} números, a soma deles é {soma - 999}!')'''

n = cont = soma = 0
n = int(input('Digite um número [999 para parar] ')) #Flag nao ira ser somado pois não ira ter 999 devido ao while. (vai sair do looping)
while n != 999:
    soma += n
    cont +=1  
    n = int(input('Digite um número [999 para parar] ' ))
print(f'Você digitou {cont-1} números, a soma deles é {soma}!')
