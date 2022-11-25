# Contando vogais com tuplas

palavras = ('aprender',
            'programar',
            'linguagem',
            'python',
            'curso',
            'gratis',
            'estudar',
            'praticar',
            'trabalhar',
            'mercado',
            'programador',
            'futuro')
vogais = ('a', 'e', 'i', 'o', 'u')
for p in palavras:
    print(f'Na palavra {p.upper()} temos ', end='')
    for le in range(0, len(p)):
        if p[le] in vogais:  # if letra da palavra está em vogais:
            print(p[le], end=' ')
    print('')

