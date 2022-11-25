from time import sleep


def maior(* num):
    print('=-' * 30)
    print('Analisando os valores passados...')
    for v in num:
        print(v, end=' ')
        sleep(0.3)
    print(f'Foram informados {len(num)} números ao todo.')
    m = num[0]
    for v in num:
        if v > m:
            m = v
    print(f'O maior valor informado foi {m}')


maior(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
maior(123, 87, 89, 54, 3, -1, 8)
