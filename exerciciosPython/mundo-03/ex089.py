# Boletim com listas compostas

dados = []
registros = []

while True:  # Registrando os dados do alunos
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    if dados[1] < 0 or dados[2] < 0 or dados[1] > 10 or dados[2] > 10:
        print('Nota inválida, dados não registrados, tente novamente...')
    else:
        registros.append(dados[:])
    dados.clear()
    while True:
        resp = input('Quer continuar? [S/N]: ')[0]
        if resp in 'NnSs':
            break
    if resp in 'Nn':
        break

print('=-' * 30, '\nNª  NOME                       MÉDIA')
print('--' * 20)

for c in range(0, len(registros)):  # Imprimindo e listando os alunos com sua numeração e média
    media = (registros[c][1] + registros[c][2]) / 2
    print(f'{c + 1}   {registros[c][0]}', ' ' * (25 - (len(registros[c][0]))), media)

print('--' * 20)
print('=-' * 30)

while True:  # Consulta das notas dos respectivos alunos, usando a numeração do aluno como chave
    opc = int(input('Consultar as notas de qual aluno? [999 interrompe] '))
    if opc == 999:
        break
    if opc > len(registros) or opc <= 0:
        print('Aluno não existe! Tente novamente...')
    else:
        print(f'As notas de {registros[opc - 1][0]} são [{registros[opc - 1][1]}, {registros[opc - 1][2]}]')
    print('--' * 30)


