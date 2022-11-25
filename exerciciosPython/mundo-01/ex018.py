# seno, cosseno e tangente

from math import sin, cos, tan, radians

angle = int(input('Digite um ângulo em graus: '))

radians = float(radians(angle))

print(f'O ângulo de {angle}º tem o seno: {sin(radians):.2f}')
print(f'O ângulo de {angle}º tem o cosseno: {cos(radians):.2f}')
print(f'O ângulo de {angle}º tem a tangente: {tan(radians):.2f}')