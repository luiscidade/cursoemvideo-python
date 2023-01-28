from ex115.lib.interface import cabecalho


def arquivo_existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado')


def ler_arquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Não foi possível ler o arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        print(a.read())
    finally:
        a.close()


def cadastrar(arq, nome, idade):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo')
    else:
        try:
            a.write(f'{nome};{idade}')
        except:
            print('Houve um ERRO ao escrever o cadastro')
        else:
            print(f'O registro de {nome} foi criado')
            a.close()
