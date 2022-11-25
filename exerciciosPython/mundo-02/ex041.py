# Classificando atletas

from datetime import date

ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano
print(f'O atleta tem {idade} anos.')

if 0 < idade <= 9:
    print('Classificação: MIRIM')
elif 9 < idade <= 14:
    print('Classificação: INFANTIL')
elif 14 < idade <= 19:
    print('Classificação: JUNIOR')
elif 19 < idade <= 25:
    print('Classificação: SÊNIOR')
elif 25 < idade:
    print('Classificação: MASTER')
else:
    print('Ano inválido.')


