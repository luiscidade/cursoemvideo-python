# Progressão aritmética v.2

a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
n_termo = int(input('Quantos termos você deseja visualizar? '))
controle = 0
while n_termo > 0:
    print(a1 + r * (n_termo - (n_termo - controle)), end='')
    controle += 1
    n_termo -= 1
    if n_termo != 0:
        print(' → ', end='')
