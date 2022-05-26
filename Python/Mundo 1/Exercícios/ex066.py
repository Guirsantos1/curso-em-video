n = s = cont = 0
while True:
    n = int(input('Digite número para somar. [999] p/ parar:' ))
    cont += 1
    if n == 999:
        break
    s += n
print(f'O total de números digitados foi {cont}. a soma entre eles é {s}')    