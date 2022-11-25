# Gerenciador de pagamentos

valor = float(input('Preço das compras: R$'))

print("""FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão""")

formapag = float(input('Qual é a opção? ')) // 1

if formapag == 1:
    print(f'Sua compra de R${valor:.2f} vai custar R${valor - (valor * 0.1):.2f} no final.')
elif formapag == 2:
    print(f'Sua compra de R${valor:.2f} vai custar R${valor - (valor * 0.05):.2f} no final.')
elif formapag == 3:
    print(f'Sua compra de R${valor:.2f} vai custar R${valor:.2f} no final')
elif formapag == 4:
    nparcelas = int(input('Quantas parcelas? '))

    if nparcelas < 3:
        print('Número de parcelas inválidas.')
        quit()

    valorparcela = (valor / nparcelas) + valor * 0.2
    print(f'Sua compra será parcelada em {nparcelas}x de R${valorparcela:.2f}.')
    print(f'Sua compra de R${valor:.2f} vai custar R${valorparcela * nparcelas:.2f} no final')
else:
    print('Opção inválida.')

