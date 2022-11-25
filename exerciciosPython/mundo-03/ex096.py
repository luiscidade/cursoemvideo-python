def area(a, b):
    m = a * b
    return m


larg = float(input('Largura (m): '))
comp = float(input('Comprimento (m): '))
print(f'O terreno com dimensões {larg}x{comp} tem como área {area(larg, comp)}m².')
