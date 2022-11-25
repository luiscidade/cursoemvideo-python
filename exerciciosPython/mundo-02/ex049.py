# Tabuada v.2

print('-=' * 21)
tb = 'Tabuada v.2'
print(' ' * 13, tb)
print('-=' * 21)

num = int(input('Digite um valor para obter sua tabuada: '))

for c in range(1, 11):
    print(f'{num:2} x {c:2} = {num * c}')
