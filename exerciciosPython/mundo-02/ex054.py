# Grupo da maioridade

from datetime import date

menor = 0
maior = 0
anoatual = date.today().year

for pessoa in range(1, 8):
    nasc = int(input(f'Digite o ano de nascimento da {pessoa}ª pessoa: '))
    idade = anoatual - abs(nasc)
    if 0 < idade < 18:
        menor += 1
    elif idade >= 18:
        maior += 1
    else:
        print('ANO INVÁLIDO')
        quit()
print(f'Maiores de idade: {maior}\n'
      f'Menores de idade: {menor}')
