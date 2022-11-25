# Cadastro de trabalhador

from datetime import datetime

dados = dict()

dados["nome"] = input('Nome: ')
dados["idade"] = int(input('Ano de nascimento: '))
dados["ctps"] = int(input('Carteira de trabalho (0 se não tem): '))
dados["idade"] = datetime.now().year - dados["idade"]
if dados["ctps"] != 0:
    dados["contratação"] = int(input('Ano de contratação: '))
    dados['salário'] = input('Salário: R$')
    dados["aposentadoria"] = dados["idade"] + ((dados["contratação"] + 35) - datetime.now().year)

print('=-' * 30)

for k, v in dados.items():
    print(f'{k} : {v}')