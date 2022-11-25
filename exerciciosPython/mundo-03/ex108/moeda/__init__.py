def aumentar(n, porcent):
    return n + (n * (porcent / 100))


def diminuir(n, porcent):
    return n - (n * (porcent / 100))


def dobro(n):
    return n * 2


def metade(n):
    return n / 2


def moeda(n, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')
