from random import randint
from time import sleep


def sorteio(lista):
    print('Sorteando valores da lista: ', end='')
    for c in range(0, 5):
        lista.append(randint(1, 10))
        print(lista[c], end=' ')
        sleep(0.3)
    print()


def somapar(lista):
    s = 0
    for c in range(len(lista)):
        if lista[c] % 2 == 0:
            s += lista[c]
    return s


numeros = []
sorteio(numeros)
print(f'Lista: {numeros}', f'Soma dos pares: {somapar(numeros)}')