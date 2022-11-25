# Dividindo valores em várias listas

lista = []
pares = []
impares = []

while True:
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    lista.append(n)
    resp = input('Quer continuar? [S/N] ').upper()[0]
    if resp in 'N':
        break
print(f'Lista de todos os valores: {lista}',
      f'\nLista dos pares: {pares}',
      f'\nLista dos ímpares: {impares}')
