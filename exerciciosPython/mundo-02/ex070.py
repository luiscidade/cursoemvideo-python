# Estatística em produto

maismil = total = maisbarato = 0
nomebarato = ''

while True:
    nome = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    if total == 0:
        maisbarato = preco
        nomebarato = nome
    if preco < maisbarato:
        maisbarato = preco
        nomebarato = nome
    if preco > 1000:
        maismil += 1
    total += preco
    while True:
        resp = input('Quer continuar? [S/N] ').upper().strip()[0]
        if resp in 'SN':
            break
    if resp in 'N':
        break
print('-' * 10, ' FIM DO PROGRAMA ', '-' * 10)
print(f'O total da compra foi R${total:.2f}\n'
      f'Temos {maismil} produtos custando mais de R$1000.00\n'
      f'O produto mais barato foi {nomebarato} custando R${maisbarato:.2f}')
