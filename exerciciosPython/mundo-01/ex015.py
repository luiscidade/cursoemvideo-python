# aluguel de carros (R$X*km rodados + R$Z*dias rodados)

dias = int(input('Dias com o carro: '))
km = float(input('Kms rodados: '))

# neste caso é cobrado R$60 por dia e R$0,15 por kms rodados

pagamento = (dias*60)+(km*0.15)

print(f'O custo total do aluguel deu: R${pagamento:.2f}')