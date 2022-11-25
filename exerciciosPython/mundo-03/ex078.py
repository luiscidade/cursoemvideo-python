# Maior e menor valor em uma LISTA

valores = []
maior = int()
menor = int()
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para posição {c}: ')))
    if c == 0:
        maior = menor = valores[0]
    else:
        if maior < valores[c]:
            maior = valores[c]
        if menor > valores[c]:
            menor = valores[c]
print('Lista: ', valores)
print(f'Menor valor: {menor}')
print(f'Maior valor: {maior}')


