n1 = float(input('Sua 1° nota: '))
n2 = float(input('Sua 2° nota: '))
media = (n1 + n2) / 2
if media <= 5:
    print(f'Sua média foi {media:.1f} você foi REPROVADO.')
elif media <= 6.9:
    print(f'Sua média foi {media:.1f} você está de RECUPERAÇÃO.')
elif media >= 7:
    print(f'Sua média foi {media:.1f} você foi APROVADO.')
