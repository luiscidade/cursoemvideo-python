# Contagem regressiva

from time import sleep

tempo = int(input('Digite um tempo em segundos para a contagem regressiva: '))

for tempo in range(tempo, -1, -1):
    if tempo >= 60:
        m = tempo//60
        seg = tempo - (m * 60)
    else:
        m = 0
        seg = tempo

    seg = int(seg)
    print(f'\r{m:02d}:{seg:02d}', end='')
    sleep(1)
    tempo -= 1
print('\n==== Contagem encerrada ====')
