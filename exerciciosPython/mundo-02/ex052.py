# Números Primos

num = int(input('Digite um número: '))
controle = 0
print('Divisivel por : ')

for c in range(1, num + 1):
    if num % c == 0:
        controle += 1
        print(f'\033[1;32m{c}\033[0m', end=' ')
    else:
        print(f'{c}', end=' ')
if controle == 2:
    print('\nÉ um número primo.')
else:
    print('\nNão é um número primo.')
