# Maior ou menor valor com tuplas e valores sorteados

from random import randint

valores = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
print('Os valores sorteados foram: ', valores)
print('O maior valor sorteado foi: ', max(valores))
print('O menor valor sorteado foi: ', min(valores))