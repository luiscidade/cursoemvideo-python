# Lista com pares e ímpares

listas = [[], []]

for c in range(1, 8):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        listas[0].append(n)
    else:
        listas[1].append(n)

print('=-' * 30)
print(f'Todos os valores: {listas[0] + listas[1]}')
print(f'Os valores pares digitados: {sorted(listas[0])}')
print(f'Os valores ímpares digitados: {sorted(listas[1])}')

