# Dicionários

aluno = dict()
aluno["nome"] = str(input('Nome: '))
aluno["média"] = float(input(f'Média de {aluno["nome"]}: '))

if 10 >= aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 7 > aluno["média"] >= 5:
    aluno['situação'] = 'Recuperação'
elif 0 < aluno["média"] < 5:
    aluno['situação'] = 'Reprovado'
else:
    print('Dados inválidos')

for k, v in aluno.items():
    print(f'O {k} é: {v}')

'''print(f'O nome é igual a {aluno["nome"]}')
print(f'A média é igual a {aluno["média"]}')
print(f'A situação é igual a {aluno["situação"]}')'''