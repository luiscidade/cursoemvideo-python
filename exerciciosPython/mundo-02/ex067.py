# Tabuada v.3

while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print("--" * 20)
    if num > 0:
        for c in range(1, 11):
            print(f'{num} x {c} = {num * c}')
    else:
        print('PROCESSO FINALIZADO')
        break
    print("--" * 20)