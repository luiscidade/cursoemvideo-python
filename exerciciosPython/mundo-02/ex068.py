# Jogo do Par ou Ímpar

from random import randint

print('VAMOS JOGAR PAR OU ÍMPAR')

score = 0
while True:
    print('=-' * 30)
    player_valor = int(input('Digite um valor: '))
    player_opcao = str(input('Par ou Ímpar [P/I]: ')).upper().strip()
    cpu_valor = randint(0, 10)
    total = player_valor + cpu_valor
    print('--' * 30)
    if player_opcao in 'PI' and player_valor >= 0:
        if total % 2 == 0:  # CASO TOTAL SEJA PAR
            if player_opcao in 'P':
                print(f'Com {player_valor} e {cpu_valor} total de {total} DEU PAR. Você VENCEU!')
                print('Vamos jogar novamente...')
                score += 1
            else:
                print(f'Com {player_valor} e {cpu_valor} total de {total} DEU PAR. Você PERDEU.')
                break
        elif total % 2 != 0:  # CASO TOTAL SEJA ÍMPAR
            if player_opcao in 'I':
                print(f'Com {player_valor} e {cpu_valor} total de {total} DEU ÍMPAR. Você VENCEU!')
                print('Vamos jogar novamente...')
                score += 1
            else:
                print(f'Com {player_valor} e {cpu_valor} total de {total} DEU ÍMPAR. Você PERDEU.')
                break
    else:
        print('OPÇÃO OU VALOR INVÁLIDO. Tente novamente...')
print('=-' * 30)
print(f'GAME OVER! Score: {score}')
