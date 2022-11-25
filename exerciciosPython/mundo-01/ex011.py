# pintando a parede (1 m² de parede = 2l de tinta)

width = float(input('Largura da parede: '))
height = float(input('Altura da parede: '))
area = width*height
print(f'A parede de dimensão {width}x{height} tem a área de {area}m² e será necessário para pintá-la completamente '
      f'{area*2}l de tinta.')
