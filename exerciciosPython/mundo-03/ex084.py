dados = []
pessoas = []
maiopeso = float(0)
menopeso = float(1000)

while True:
    dados.append(input('Nome: '))
    dados.append(float(input('Peso (em kg): ')))
    pessoas.append(dados[:])

    if dados[1] > maiopeso:
        maiopeso = dados[1]
    if dados[1] < menopeso:
        menopeso = dados[1]

    dados.clear()

    resp = str(input('Quer continuar? [Digite 0 se não] : '))[0]
    if resp in '0':
        break

pessoas_maiopeso = []
pessoas_menopeso = []

for dado in pessoas:
    if dado[1] == maiopeso:
        pessoas_maiopeso.append(dado[0])
    if dado[1] == menopeso:
        pessoas_menopeso.append(dado[0])

print('-=' * 30)
print(f'Ao todo você cadastrou {len(pessoas)} pessoa(s)')
print(f'O maior peso registrado foi {maiopeso} kg. Peso de {pessoas_maiopeso}')
print(f'O menor peso registrado foi {menopeso} kg. Peso de {pessoas_menopeso}')
