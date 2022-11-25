# Extraindo dados de um lista

lista = []

while True:
    lista.append(int(input('Digite um valor: ')))
    while True:
        resp = input('Quer continuar? [S/N] ').upper()[0]
        if resp in 'NS':
            break
    if resp in 'N':
        break

lista.sort(reverse=True)

print(f'Você digitou {len(lista)} elemento(s).')
print(f'Os valores em ordem decrescente ficam: {lista}')
if 5 in lista:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista')