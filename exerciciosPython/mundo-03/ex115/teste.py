
from time import sleep
from ex115.lib.interface import *
from arquivo import *


class Main:

    def __init__(self):

        while True:
            resposta = menu(['Listar cadastrados', 'Cadastrar Pessoa', 'Sair do sistema'])

            if resposta == 1:
                ler_arquivo('arquivo.txt')
            elif resposta == 2:
                cabecalho('NOVA CADASTRO')
                nome = input('Nome: ')
                idade = leiaInt('Idade: ')
                cadastrar('arquivo.txt', nome, idade)
            elif resposta == 3:
                cabecalho('Saindo do sistema...')
                break
            else:
                print('Opção inválida! Tente novamente...')
            sleep(2)


if __name__ == '__main__':
    help(min)

