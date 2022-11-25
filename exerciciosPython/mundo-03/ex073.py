# Times do brasileirão

times = ('Palmeiras', 'Internacional', 'Flamengo', 'Fluminense', 'Corinthians', 'Athletico-PR', 'Atlético-MG',
         'América-MG', 'Goiás', 'Santos', 'Bragantino', 'Botafogo', 'São Paulo', 'Ceára SC', 'Fortaleza', 'Coritiba',
         'Cuiabá', 'Avaí', 'Atlético-GO', 'Juventude')
print('Tabela do Brasileirão 2022 (rodada 26)')
for c in range(0, len(times)):
    print(f'{c + 1:02d}  {times[c]}')
print(f'\nOrdem alfabética: {sorted(times)}\n',
      f'Os 4 primeiros: {times[0:5]}\n',
      f'Os 4 últimos: {times[16:20]}')
