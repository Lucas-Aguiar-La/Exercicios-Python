# Jogo da Adivinhação v.1.0:
from random import randint
from time import sleep
print('--=--' * 6)
print('    JOGO DA ADIVINHAÇÃO')
print('--=--' * 6)
print('Irei pensar em um número\n'
      'de 0 a 5 e você só tem que\n'
      'adivinhar que número que foi!\n')
sleep(5)
player = int(input('Vamos lá, que número eu pensei? '))
pc = randint(0,5)
print('Processando...\n')
sleep(3)
if player == pc:
    print('Você ACERTOU!\n '
          f'Eu pensei no número {pc}!\n'
          ' Droga...')
else:
    print('Você ERROU!\n'
          f'Eu pensei no número {pc} e não no {player}!\n'
          'Ha ha ha, mais sorte na próxima!')
print('--=--' * 6)
print('  J O G O  F I N A L I Z A D O')
print('--=--' * 6)