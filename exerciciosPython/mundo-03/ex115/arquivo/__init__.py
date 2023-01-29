from lib.interface import cabecalho


def arquivo_existe(arq):
    try:
        a = open(arq, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(arq):
    try:
        a = open(arq, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {arq} criado')


def ler_arquivo(arq):
    try:
        a = open(arq, 'rt')
    except:
        print('Não foi possível ler o arquivo!')
    else:
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
            a.write(f'{nome}  {idade}\n')
        except:
            print('Houve um ERRO ao escrever o cadastro')
        else:
            print(f'O registro de {nome} foi criado')
            a.close()
            

def limpar_arquivo(arq):
    try:
        a = open(arq, 'w')
        a.close()
    except:
        print("Ocorreu um erro ao limpar o arquivo!")
