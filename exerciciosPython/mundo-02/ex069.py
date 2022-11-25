# Análise de grupos

maioridade = 0
qt_hm = 0
qt_ml_20 = 0

while True:
    print('-' * 31)
    print(' ' * 4, 'CADASTRE UMA PESSOA')
    print('-' * 31)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    if idade > 0 and sexo in 'MF':  # Barreira contra idade negativas e sexos inválidos
        if idade > 18:
            maioridade += 1
        if sexo in 'M':
            qt_hm += 1
        if sexo in 'F' and idade < 20:
            qt_ml_20 += 1
        print('-' * 31)
        while True:  # controle da váriável de continuar ou parar o WHILE DE CADASTRO, o looping encer quando 'N' ou 'S'
            cadastromais = str(input('Quer continuar? [S/N] ')).strip().upper()
            if cadastromais in 'NS':
                break
            else:
                print('Opção inválida!')
        if cadastromais in 'N':
            break
    else:
        print('IDADE OU SEXO INVÁLIDOS! Tente novamente...')
print('-' * 31)
print(f'Total de pessoas com mais de 18 anos: {maioridade}\n'
      f'Quantidade de homens cadastrados: {qt_hm}\n'
      f'Quantidade de mulheres com menos de 20 anos cadastradas: {qt_ml_20}\n')

