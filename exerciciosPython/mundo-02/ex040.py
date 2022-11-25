# Média

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1+nota2)/2

print(f'Tirando {nota1:.1f} e {nota2:.1f}, a média do aluno é {media:.1f}')

if 10 >= media >= 7:
    print('O aluno está APROVADO.')
elif 5 <= media <= 6.9:
    print('O aluno está em RECUPERAÇÃO.')
elif 0 <= media < 5:
    print('O aluno está REPROVADO.')
else:
    print('Nota inválida.')
    quit()

