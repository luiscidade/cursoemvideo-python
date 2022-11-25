# Analisador de Textos

nome = input('Digite seu nome: ').strip()

print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}\n',
      f'Seu nome em minúsculas é {nome.lower()}\n',
      f'Seu nome tem {len(nome) - nome.count(" ")}\n',
      f'Seu primeiro nome é {nome.split()[0]}')
