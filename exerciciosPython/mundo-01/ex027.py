# identificar o primeiro e o ultimo nome

nome = str(input('Digite o nome completo: ')).title().strip().split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('E o seu último nome é {}'.format(nome[len(nome)-1]))

# Dica:
# o [-1] pode ser utilizado para se referir ao último objeto de uma lista,
# assim como [-2] seria a penúltima e assim por diante.
#
# print('E o seu último nome é {}'.format(nome[-1]))
