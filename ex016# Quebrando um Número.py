# Quebrando um Número:
import math
sub = '\033[4m'
verde = '\033[32m'
end = '\033[m'
valor = float(input('Digite um valor: '))
#porção_inteira = int(valor)
print(f'O valor digitado foi {sub}{valor}{end} e sua'
      f'porção inteira é {verde}{valor.__trunc__()}{end}!')
