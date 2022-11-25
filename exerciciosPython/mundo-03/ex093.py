# Cadastro jogador de futebol com dicionários

jogador = dict()

jogador["nome"] = input('Nome do jogador: ')
jogador["partidas"] = int(input(f'Quantos partidas {jogador["nome"]} jogou? '))
jogador["gols"] = []
jogador["total"] = 0

for p in range(0, jogador["partidas"]):
    jogador["gols"].append(int(input(f'  Quantos gols na partida {p}? ')))
    jogador["total"] += jogador["gols"][p]

print('=-' * 30)

print(jogador)

print('=-' * 30)

for k, v in jogador.items():
    print(f'No campo {k} temos {v}')

print('=-' * 30)

print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')

for p in range(0, jogador["partidas"]):
    print(' ' * 4, f'=> Na partida {p} fez {jogador["gols"][p]} gols')
print(f'Foi um total de {jogador["total"]} gols')
