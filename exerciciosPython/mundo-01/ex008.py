# conversor de medidas

x = float(input('Uma distância em metros: '))
print(f'A medida de {x}m corresponde a '
      f'\n'
      f'{x/1000}km\n'
      f'{x/100}hm\n'
      f'{x/10}dam\n'
      f'{x*10}dm\n'
      f'{x*100}cm\n'
      f'{x*1000}mm'
      )
