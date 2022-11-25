# calculando descontos

import sys

produto = float(input('Quanto custa o produto? R$'))
desconto = int(input('O desconto é de quanto porcento (%): '))

if desconto < 0 or desconto > 100:
    print('Desconto inválido.')
    sys.exit()

print(f'O produto que custava R${produto:.2f}, na promoção com desconto de {desconto}% vai custar '
      f'R${produto-(produto*(desconto/100)):.2f}')
