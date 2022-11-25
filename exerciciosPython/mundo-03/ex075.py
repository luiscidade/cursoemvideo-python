# Análise de dados em uma Tupla

print('ANÁLISE DE DASOS EM UM TUPLA')


while True:
    metodo = int(input('Método 1 ou 2? '))
    if metodo == 1:

        # Meu método ->

        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
        n3 = int(input('Digite mais um número: '))
        n4 = int(input('Digite o último número: '))

        numeros = (n1, n2, n3, n4)
        pares = 0
        print(f'\nValores digitados: {numeros}')
        print(f'O valor 9 apareceu {numeros.count(9)} vezes')
        for n in range(0, 4):
            if numeros[n] == 3:
                print('O 3 está na posição', n)
            if numeros[n] % 2 == 0:
                pares += 1
        print(f'Os valores pares digitados foram {pares}')
        break

    elif metodo == 2:

        # Método do curso em vídeo (Método correto)

        num = (int(input('Digite um número: ')),
               int(input('Digite outro número: ')),
               int(input('Digite mais um número: ')),
               int(input('Digite o último número: ')))
        print(f'O número 9 aparece {num.count(9)} vezes')
        if 3 in num:
            print(f'A primeira vez que aparece o 3, aparece na posição {num.index(3) + 1}')
        else:
            print('O valor 3 não foi inserido')
        print('Os valores pares digitados foram ', end='')
        for n in num:
            if n % 2 == 0:
                print(n, end=' ')
        break

