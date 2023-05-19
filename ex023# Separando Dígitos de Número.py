# Separando Dígitos de Número:
from time import sleep
azul = '\033[34m'
sub = '\033[4m'
verde = '\033[32m'
end = '\033[m'
num = int(input('Digite um número: '))
print(f'{azul}Analisando o número {num}...{end}')
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
sleep(2)
print(f'{sub}Unidade{end}: {verde}{u}{end}\n'
      f'{sub}Dezena{end}: {verde}{d}{end}\n'
      f'{sub}Centena{end}: {verde}{c}{end}\n'
      f'{sub}Milhar{end}: {verde}{m}{end}')
