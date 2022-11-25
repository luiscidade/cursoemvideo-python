def ficha(nome='', n_gols=''):
    if len(nome) == 0:
        nome = '<desconhecido>'
    if len(n_gols) == 0:
        n_gols = '0'
    if n_gols.isnumeric():
        n_gols = int(n_gols)
        print(f'O jogador {nome} fez {n_gols} gol(s) no campeonato')
    else:
        print('ERRO')


# Programa iniciado

jogador = input('Nome do jogador: ').strip()
gols = input(f'Quantos gols fez o jogador? ').strip()

ficha(n_gols=gols)
