# Matriz com análise de dados

matriz = [[], [], []]
soma_par = soma_3colu = 0

for l in range(0, 3):  # Leitura da matriz
    for c in range(0, 3):
        matriz[l].append(int(input(f'Digite um valor para [{l}, {c}]: ')))

for l in range(0, 3):  # Printando a matriz de forma organizada
    print()
    for c in range(0, 3):
        print(f'{matriz[l][c]:^5}', end='')

for l in range(0, 3):  # Análise de dados
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            soma_par += matriz[l][c]
        if c == 2:
            soma_3colu += matriz[l][c]

print('\n')
print(f'A soma dos valores pares da matriz é {soma_par}')
print(f'A soma da terceira coluna da matriz é {soma_3colu}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')
