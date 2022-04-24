altura = float(input('Digite a sua altura:(m) '))
peso = float(input('Digite o seu peso:(Kg) '))
imc = peso / (altura**2)
print(f'Seu IMC é de {imc:.1f}')
if imc < 18.5:
    print('Você está abaixo do peso')
elif 25 > imc > 18.5:
    print('PESO IDEAL')
elif 30 > imc >= 25:
    print('SOBRE PESO')
elif 40 > imc >= 30:
    print('OBESIDADE')
else:
    print('OBESIDADE MÓRBIDA')