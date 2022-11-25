

velocidade = float(input('Qual é a velocidade atual do carro (em km/h)? ')) // 1
multa = 7

if velocidade > 80:
    print(f'VOCE FOI MULTADO COM O VALOR DE R${multa*(velocidade-80):.2f}! Dirija com mais segurança.')
if 0 < velocidade <= 80:
    print('Siga em frente.')
if velocidade < 0:
    print('Tá na contra-mão cidadão?')
