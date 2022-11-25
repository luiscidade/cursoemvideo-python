# Fatorial

n = int(input('Digite um número\n'
              'para calcular seu fatorial: '))

a = 1
for c in range(n, 0, -1):
    a *= c
    print(f'{c} x', end=' ')
print(f'= {a}')

