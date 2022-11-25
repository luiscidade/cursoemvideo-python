# Jogo de dados em Python

from random import randint
from operator import itemgetter


jogadores = dict()
biggestvalue = 0
print('Valores sorteados:')

for c in range(0, 4):
    jogadores[f"jogador{c+1}"] = randint(1, 6)
for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for c in range(1, 5):
    print(f'{c}ª  {ranking[c-1][0]}')
    