# Analisador completo

soma_idade = 0
maior_idade = 0
mulheres_20 = 0
sexo_maior = ''
nome_maior = ''

for pessoa in range(1, 5):
    print('-'*5, f'{pessoa}ª PESSOA', '-'*5)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    soma_idade += idade
    if idade > maior_idade:
        maior_idade = idade
        nome_maior = nome
        sexo_maior = sexo
    if sexo == 'F':
        if idade < 20:
            mulheres_20 += 1

# Média

print(f'A média de idade do grupo é {soma_idade/4} anos')

# Homem ou mulher mais velha(o)

if sexo_maior == 'M':
    print(f'O homem mais velho tem {maior_idade} anos e se chama {nome_maior}')
elif sexo_maior == 'F':
    print(f'A mulher mais velha tem {maior_idade} anos e se chama {nome_maior}')
else:
    print(f'SEXO INVÁLIDO')

print(f'Ao todo são {mulheres_20} mulheres com menos de 20 anos')
