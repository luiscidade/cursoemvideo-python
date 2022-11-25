# Conversão decimal para: binário, octal e hexadecimal

num = int(input('Digite um valor inteiro: '))
controle = int(input("""Digite a opção desejada:
[ 1 ] para converter para binário
[ 2 ] para converter para octal
[ 3 ] para converter para hexadacimal
Sua opção: """))

if controle == 1:
    print(f'{num} em BINÁRIO é igual a: {bin(num)[2:]}')
elif controle == 2:
    print(f'{num} em OCTAl é igual a: {oct(num)[2:]}')
elif controle == 3:
    print(f'{num} em HEXADECIMAL é igual a: {hex(num)[2:]}')
else:
    print('Opção inválida!')
    quit()