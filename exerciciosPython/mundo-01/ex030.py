# Par ou Impar

num = float(input('Digite um valor: ')) // 1
parouimpar = num % 2

if parouimpar == 0:
    print(f'{num:.0f} é PAR')

if parouimpar == 1:
    print(f'{num:.0f} é IMPAR')
