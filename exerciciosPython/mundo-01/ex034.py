# Aumentos múltiplos

salario = float(input('Informe seu salário: R$'))

if salario > 1250:
    print(f'Seu salário que era R${salario:.2f} aumentou e agora é R${salario+(salario*0.1):.2f}')
if 0 < salario <= 1250:
    print(f'Seu salário que era R${salario:.2f} aumentou e agora é R${salario+(salario*0.15):.2f}')
