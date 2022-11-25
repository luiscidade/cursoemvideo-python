# Voto

def voto(nasc):
    idade = 2022 - nasc
    if 0 < idade < 16:
        return 'NEGADO'
    elif 16 < idade < 18 or 65 < idade:
        return 'OPCIONAL'
    elif 18 < idade < 65:
        return 'OBRIGATORIO'


# Programa iniciado

ano = int(input('Ano de nascimento: '))
idade = 2022 - ano
if idade < 0:
    print('Ano de nascimento inválido.')
else:
    print(f'Como {idade} anos seu voto é {voto(ano)}')

