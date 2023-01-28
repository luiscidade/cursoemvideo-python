# ex104 com try, exception

def leiaInt(txt=''):
    while True:
        try:
            a = int(input(txt))
        except (TypeError, ValueError):
            print('ERRO! Por favor digite um número inteiro.')
        except KeyboardInterrupt:
            print('O usuário preferiu não declarar.')
            return 0
        else:
            return a


def leiaFloat(txt=''):
    while True:
        try:
            a = float(input(txt))
        except (TypeError, ValueError):
            print('ERRO! Por favor digite um número real.')
        except KeyboardInterrupt:
            print('\nO usuário preferiu não declarar.')
            return 0
        else:
            return a


# Programa iniciado

n = leiaInt('Digite um número inteiro: ')
f = leiaFloat('Digite um número real: ')

print('--' * 15)

print(f'O número int: {n}\n'
      f'O número float: {f}')
