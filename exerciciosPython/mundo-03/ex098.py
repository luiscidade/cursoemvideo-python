from time import sleep


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if inicio > fim and passo > 0:
        passo = -passo

    print(f'Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}')

    for c in range(inicio, fim+passo, passo):
        print(c, end=' ', flush=True)
        sleep(0.3)
    print('\n')


# Programa iniciado
contador(1, 10, 1)
contador(10, 0, 2)

i = int(input('Ínicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
print()

contador(i, f, p)