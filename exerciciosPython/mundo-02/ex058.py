# joga da advinhação 2.0

# Minha versão

from random import randint

print('Sou seu computador...\n'
      'Acabei de pensar em um número de 0 a 10\n'
      'Será que você advinha qual foi?')

cpu = randint(0, 10)
player = int(input('Qual o seu palpite? '))
tentativas = 1

while cpu != player:
      if player < cpu:
            print('Mais... Tente mais uma vez')
      elif player > cpu:
            print('Menos... Tente mais uma vez')
      else:
            print('Opção inválida! Tente novamente.')
      player = int(input('Qual o seu palpite? '))
      tentativas += 1

print(f'Acertou com {tentativas} tentativas. Parabéns!')



