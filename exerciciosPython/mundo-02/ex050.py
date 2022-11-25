# Soma dos pares (ler seis numeros, descobrir os pares e depois somá-los)

soma = 0

for c in range(1, 7):
    num = int(input(f'Número {c}: '))
    if num % 2 == 0:
        soma += num

print('\nA soma dos números pares é igual a:', soma)
