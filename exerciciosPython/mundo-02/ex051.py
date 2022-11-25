# Progressão Aritmética

a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
soma = 0

for c in range(0, 10):
    termo = a1 + (c*r)
    print(f'{termo}', end=' → ')
    soma += termo

print('Acabou')
print(f'E soma entre eles é igual a: {soma}')
