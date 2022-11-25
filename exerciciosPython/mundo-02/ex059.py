# Criando um menu de opções]

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
sair = False

while not sair:
    print('     [ 1 ] somar\n'
          '     [ 2 ] multiplicar\n'
          '     [ 3 ] maior\n'
          '     [ 4 ] novos números\n'
          '     [ 5 ] sair do programa')

    opcao = int(input('>>>>> Qual a sua opção? '))

    if opcao == 1:
        print(n1+n2)
    elif opcao == 2:
        print(n1*n2)
    elif opcao == 3:
        if n1-n2 < 0:
            print(f'{n2} é maior')
        else:
            print(f'{n1} é maior')
    elif opcao == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        sair = True
    else:
        print('Opção inválida! Tente novamente.')
