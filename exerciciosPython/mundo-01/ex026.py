# Primeira e a ultima ocorrência em uma string

frase = str(input('Digite uma frase: ')).strip().lower().replace('á', 'a').replace('ã', 'a').replace('â', 'a')

print(f'A frase tem {len(frase)} posições (contando os espaços).')
print('A letra A aparece {} vezes na frase.'.format(frase.count('a')))
print('A primeira letra A aparece na posição {}.'.format(frase.find('a')+1))
print('A última letra A aparece na posição {}'.format(frase.rfind('a')+1))
