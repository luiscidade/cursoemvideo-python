def aumentar(n, porcent, formato=False):
    res = n + (n * (porcent / 100))
    if not formato:
        return res
    else:
        return moeda(res)


def diminuir(n, porcent, formato=False):
    res = n - (n * (porcent / 100))
    if not formato:
        return res
    else:
        return moeda(res)


def dobro(n, formato=False):
    res = n * 2
    if not formato:
        return res
    else:
        return moeda(res)


def metade(n, formato=False):
    res = n / 2
    if not formato:
        return res
    else:
        return moeda(res)


def moeda(n, m='R$'):
    return f'{m}{n:.2f}'.replace('.', ',')


def resumo(p, a, d):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado:\t{moeda(p)}')
    print(f'Dobro do preço: \t{dobro(p, True)}')
    print(f'Metade do preço: \t{metade(p, True)}')
    print(f'Aumento de {a}%: \t{aumentar(p, a, True)}')
    print(f'Diminuição de {d}%:\t{diminuir(p, d, True)}')
    print('-' * 30)
