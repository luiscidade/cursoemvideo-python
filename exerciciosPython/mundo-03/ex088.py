# Jogo da mega sena

from random import randint
from time import sleep

jogo = []
jogos = []

r = int(input('Quantos jogos você quer que eu sorteie? '))
for c in range(r):
    while len(jogo) != 6:
        n = randint(0, 60)
        if n not in jogo:
            jogo.append(n)
    print(f'Jogo {c + 1}: {sorted(jogo)}')
    sleep(1)
    jogos.append(sorted(jogo[:]))  # Registro de todos os jogos em ordem
    jogo.clear()
print(f'Todos os jogos: {jogos}')