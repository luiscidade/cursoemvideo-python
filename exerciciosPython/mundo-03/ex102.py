# Fatorial com funções

def fatorial(a, show=False):
    """
    > Calcular fatorial de um número

    :param a: número a ser fatorizado. (a!)
    :param show: (opcional) mostrar o cálculo ou não
    :return f: resultado do fatorial
    """
    f = 1
    for c in range(a, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# Programa iniciado

print(fatorial(6, True))
