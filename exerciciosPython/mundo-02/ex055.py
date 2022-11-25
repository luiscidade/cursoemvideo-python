# Maior e menor sequência

maior = 0
menor = 0

for pessoa in range(1, 6):
    peso = float(input(f'Peso da {pessoa}ª pessoa: '))
    if pessoa == 1:
        menor = peso
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('='*21)
print(f'\033[1mMaior peso: {maior}\n'
      f'Menor peso: {menor}\033[0m')
print('='*21)