# menu antigo?

def menu():
    while True:
        print('--' * 30)
        print('MENU PRINCIPAL'.center(60))
        print('--' * 30)
        print(' 1 - Ver pessoas cadastradas')
        print(' 2 - Cadastrar nova Pessoa')
        print(' 3 - Sair do Sistema')
        print('--' * 30)
        while True:
            try:
                op = int(input('Sua opção: '))
                if op == 1:
                    print('--' * 30)
                    print('Opção 1'.center(60))
                    print('--' * 30)
                    break
                elif op == 2:
                    print('--' * 30)
                    print('Opção 2'.center(60))
                    print('--' * 30)
                    break
                elif op == 3:
                    print('Saindo do sistema...')
                    quit()
                else:
                    print('Por favor selecione uma opção válida')

            except (ValueError, TypeError):
                print('Tipo inválido! Por favor tente novamente...')

            except KeyboardInterrupt:
                print('\nO usuário quitou do sistema!')
                quit()