# Alistamento militar

from datetime import date

ano = int(input('Ano de nascimento: '))
anoatual = date.today().year
idade = anoatual-ano

print(f'Quem nasceu em {ano} faz {idade} anos em {anoatual}')

if idade < 18:
    print(f'Você terá que se alistar daqui a {18-idade} anos. No ano {ano+18}')
elif idade > 18:
    print(f'Você deveria se alistar a {idade-18} anos atrás. No ano {ano+18}')
else:
    print('Você deverá se alistar esse ano!')