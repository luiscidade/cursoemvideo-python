# Listagem de preços

print('==' * 34, '\n',
      ' ' * 21, 'LISTAGEM DE PREÇOS')
print('--' * 34)

produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
            'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90, 'Apontador', 3.00)
for c in range(0, len(produtos)):
    if c % 2 == 0:
        print(f'{produtos[c]}', '.' * (56 - (len(produtos[c]))), 'R$ ', end='')
    else:
        print(f'{produtos[c]:6.2f}')
print('--' * 34)
