# Validação de dados

# Minha versão

sexo = input('Informe seu sexo [M/F]: ').strip().upper()
while sexo != 'M' and sexo != 'F':
    sexo = input('Dados inválidos, por favor insira seu sexo: ').strip().upper()
print(f'Sexo {sexo} registrado com sucesso')

# Versão do Curso em Vídeo

sexo = input('Informe seu sexo [M/F]: ').strip().upper()[0]  # pega só a primeira letra com [0]
while sexo not in 'MmFf':  # pesquisar mais a sintaxe 'not in'
    sexo = input('Dados inválidos, por favor insira seu sexo: ').strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso')
