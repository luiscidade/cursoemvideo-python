# Identificar se tem Silva no nome

nome = str(input('Digite o nome completo: ')).title().strip().split()
print('Você tem "Silva" no nome? : {}'.format('Silva' in nome))
