# Aprovando empréstimos

valor = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o sua renda mensal: R$'))
anos = float(input('Em quantos anos você pretende pagar o empréstimo? '))

prestacao = valor / (anos * 12)

if prestacao >= salario-(salario * 0.7):
    print(f'A prestação do empréstimo excede 30% do sua renda mensal de R${salario:.2f}, '
          f'portanto \033[31mEMPRESTIMO NEGADO\033[m.')
else:
    print(f'\033[32mEMPRESTIMO APROVADO\033[m, '
          f'prestações serão do valor de R${prestacao:.2f} pagas durante {anos * 12:.0f} meses.')
