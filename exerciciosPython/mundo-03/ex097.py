def escreva(txt):
    print('~' * (len(txt) + 4))
    print(f'  {txt}')
    print('~' * (len(txt) + 4))
    print()


for c in range(0, 3):
    msg = input('Digite uma frase: ')
    escreva(msg)