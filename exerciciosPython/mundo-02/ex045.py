# pedra, papel e tesoura

from random import randint
from time import sleep

itens = ('Ameno', 'Pedra', 'Papel', 'Tesoura')

print('Bem vindo ao jokenpô! Você competirá com a CPU.')
print("""Suas opções:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA""")
player = int(input('Então...?  '))

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ!')

cpu = randint(1, 3)
print('\033[1m-=' * 11)
print(f'Player escolheu {itens[player]}')
print(f'CPU escolheu {itens[cpu]}')
print('-=' * 11, '\033[m')

if cpu == 1:
    if player == 1:
        print('EMPATE.')
    elif player == 2:
        print('JOGADOR VENCE')
    elif player == 3:
        print('CPU VENCE')
    else:
        print('JOGADA INVÁLIDA.')
elif cpu == 2:
    if player == 1:
        print('CPU VENCE')
    elif player == 2:
        print('EMPATE')
    elif player == 3:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif cpu == 3:
    if player == 1:
        print('JOGADOR VENCE')
    elif player == 2:
        print('CPU VENCE')
    elif player == 3:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')