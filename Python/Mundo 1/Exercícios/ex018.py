import math
a = int(input('Digite o ângulo:'))
sen = math.sin(math.radians(a))
cos = math. cos(math.radians(a))
tang = math. tan(math.radians(a))
print (
    f'O ângulo {a} tem o seno de: {sen:.2f}\n'
    f'O ângulo {a} tem o cosseno de: {cos:.2f}\n'
    f'O ângulo {a} tem a tangente de: {tang:.2f}\n'
)