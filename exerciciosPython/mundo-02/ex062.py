# Progressão aritmética v.3

a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
total_termo = int(input('Quantos termos você deseja visualizar? '))
controle = 0
while total_termo > 0:
    print(a1 + r * (total_termo - (total_termo - controle)), end='')
    controle += 1
    total_termo -= 1
    if total_termo != 0:
        print(' → ', end='')
    else:
        print(' → PAUSA', end='')
        maistermo = int(input('\nQuantos termos você deseja mostrar mais? '))
        if maistermo > 0:
            total_termo += maistermo
print(f'Progressão finalizada com {controle} termos mostrados.')
