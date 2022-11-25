# Analisando o triângulo v1.0

print('Digite os lados de um triângulo para saber se é possível formar um triângulo.')

l1 = float(input('Primeiro lado: '))
l2 = float(input('Segundo lado: '))
l3 = float(input('Terceiro lado: '))

if abs(l1 - l2) < l3 < l1 + l2 and abs(l1 - l3) < l2 < l1 + l3 and abs(l3 - l2) < l1 < l3 + l2:
    print('Triângulo possível')
    if l1 == l2 == l3:
        print('Triângulo equilátero.')
    elif l1 == l2 != l3 or l2 == l3 != l1 or l1 == l3 != l2:
        print('Triângulo isósceles.')
    elif l1 != l2 != l3:
        print('Triângulo escaleno.')
else:
    print('Triângulo não possível')
