# Valores únicos em uma lista

lista = []
valor = 0

while True:
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
    else:
        print('Valor inválido! Não vou adicionar...')
    while True:
        resp = input('Quer continuar? [S/N] ').upper().strip()[0]
        if resp in 'SN':
            break
    if resp in 'N':
        break
print(sorted(lista))
