# Unindo dicionários e listas

from operator import itemgetter

dados = dict()
registros = list()
sum_age = 0

while True:  # Registrando dados (nome, sexo e idade)
    dados["nome"] = input('Nome: ').strip()

    while True:
        dados["sexo"] = input('Sexo [M/F]: ')[0].strip().upper()

        if dados["sexo"] not in 'MF':
            print('ERRO! Por favor, digite M ou F.')
        else:
            break

    dados["idade"] = int(input('Idade: '))

    sum_age += dados["idade"]
    registros.append(dados.copy())
    dados.clear()

    while True:
        resp = input('Quer continuar? [S/N]: ')[0].upper()
        if resp in 'SN':
            break
        else:
            print('ERRO! Responda S ou N.')
    if resp in 'N':
        break

media = sum_age / len(registros)
print(f'Ao todo temos {len(registros)} pessoas cadastradas.')
print(f'A média das idades é de {media} anos.')
print('As mulheres: ', end='')
for dado in registros:
    if dado["sexo"] == 'F':
        print(f'{dado["nome"]}', end=' ')
print('\nLista de maiores que média de idade: ')
for dado in registros:
    if dado["idade"] > media:
        for k, v in dado.items():
            print(f'{k} = {v}', end='   ')



