

def leiaDinheiro(string):

    while True:
        v = input(f'{string}')
        if v.isalnum() or v.isspace() or v == '' or v.isascii():
            print(f'ERRO: "{v}" é um preço inválido')
        else:
            break

    v = v.replace(',', '.')
