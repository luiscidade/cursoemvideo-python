# Validando expressões matemáticas

expr = input('Digite uma expressão: ')
pilha = []
for simb in expr:  # simb vai assumir um espaço [de 0 até o len da string] a cada looping.
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida')
else:
    print('Sua expressão está inválida')
