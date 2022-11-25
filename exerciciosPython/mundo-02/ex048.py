# Soma ímpares e múltiplos de três

soma = 0
cont = 0

for c in range(3, 500, 6):
    soma += c
    cont += 1

print('E a soma entre eles é:', soma)
print(f'Foram somados {cont} números')
