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
