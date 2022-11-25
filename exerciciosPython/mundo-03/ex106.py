# Interactive help


while True:
    fubi = input('Função ou Blibioteca > ').lower().strip()
    if fubi == 'fim':
        print('Processo finalizado!')
        break
    help(fubi)
