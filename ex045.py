# GAME: Pedra, Papel e Tesoura:
import random
print('Suas opções:\n'
      '[ 1 ] PEDRA\n'
      '[ 2 ] PAPEL\n'
      '[ 3 ] TESOURA')
player = int(input('Qual a sua jogada? '))
opcoes = 'PEDRA', 'PAPEL', 'TESOURA'
pc = random.choice(opcoes)
print(f'{pc}')
