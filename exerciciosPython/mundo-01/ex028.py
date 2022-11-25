# Jogo de Advinhação

import random
import sys
from time import sleep

print('-=-' * 20)
print('Eu te desafio! Escolherei um número de 0 a 5, tente advinhar!')
print('-=-' * 20)

cpu = random.randint(0, 5)
player = float(input('Escolha o número de 0 a 5: ')) // 1


print('PROCESSANDO', end='')

for numero in range(3):
    if numero == 2:
        print('.')
        sleep(0.7)
    else:
        print('.', end='')
        sleep(0.7)

if player > 5 or player < 0:
    print(f'Valor inválido! {player:.0f}')
    sys.exit()

if cpu == player:
    print(f'A cpu escolheu {cpu}, e você escolheu {player:.0f}. Parabéns, você venceu!')
else:
    print(f'A cpu escolheu {cpu} e você {player:.0f}. Você perdeu.')
