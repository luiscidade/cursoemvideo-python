# conversor de moedas

carteira = float(input('Quanto você tem na carteira? R$'))

# cotações (1 moeda estrangeira = x reais)

usd = 4.88
iene = 0.038
euro = 5.15

# conversão

print(f'Com R${carteira:.2f} você pode comprar: \n')
print(f'US${carteira/usd:.2f} (dolár americano)')
print(f'€{carteira/euro:.2f} (euro)')
print(f'¥{carteira/iene:.2f} (iene japonês)')

