# Matriz

matriz = [[], [], []]

for c in range(0, 3):  # c -> linhas, d -> colunas
    for d in range(0, 3):
        matriz[c].append(int(input(f'Digite o valor para [{c}, {d}]: ')))

for c in range(0, 3):
    print()
    for d in range(0, 3):
        print(f'{matriz[c][d]:^5}', end='  ')

