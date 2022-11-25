# Ordenar lista sem repetições

lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
        pos += 1
print('-=' * 30)
print(f'Os valores inseridos em ordem crescente ficam: {lista}')

''' Tive dois erros nesse exercício: 
    - NÃO PENSAR EM USAR O MÉTODO INSERT NA LISTA
    - NÃO PENSAR EM ABSORVER O VALOR EM UMA VARIÁVEL SEPARADA ANTES DE ADICIONA-LA EM UMA LISTA'''






'''
lista = [1, 5, 9, 11, 15]
x = 0
print('Lista atual: ', lista)

lista.append(int(input('Digite um valor: ')))
valor = lista[5]

while valor > lista[x]:  # encontrado o local onde o valor inserido vai entrar
   x += 1

controle = 5 - x  # quantidade de vezes que vai ser repetida o while a seguir
y = 5  # len(lista) - 1
z = 4  # len(lista) - 2

while controle > 0:
    lista[y] = lista[z]
    controle -= 1
    y -= 1
    z -= 1

lista[x] = valor
print('Lista nova: ', lista)
'''











