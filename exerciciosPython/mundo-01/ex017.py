# catetos e hipotenusa

from math import hypot

# maneira 1, com módulo math

cop = float(input('Cateto oposto: '))
cad = float(input('Cateto adjacente: '))

print(f'Hipotenusa: {hypot(cop, cad)}')

# maneira 2, com sem qualquer módulo

print(f'\nHipotenusa: {((cop**2)+(cad**2))**(1/2)}')
