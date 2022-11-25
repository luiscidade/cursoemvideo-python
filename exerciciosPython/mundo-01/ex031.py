# Custo de viagem

distancia = float(input('Qual a distancia da viagem (em km)? '))

if 0 < distancia <= 200:
    custo = distancia * 0.5
    print(f'Sua viagem custará R${custo:.2f}')
if distancia > 200:
    custo = distancia * 0.45
    print(f'Sua viagem custará R${custo:.2f}')
if distancia < 0:
    print('Distancia Inválida.')
    quit()
