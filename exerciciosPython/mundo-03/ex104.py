def leiaint(txt=''):
    while True:
        a = input(txt).strip()
        if a.isnumeric():
            break
        else:
            print('ERRO! Por favor, digite um NÚMERO')
    a = int(a)
    return a


# Programa iniciado

n = leiaint('Digite um número: ')
print(f'O número digitado foi {n}')