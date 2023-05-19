# Média Aritimética:
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
verde = '\033[32m'
vermelho = '\033[31m'
end = '\033[m'
if m >= 7:
    print(f'{verde}PARABÉNS{end}! Sua média foi {verde}{m}{end}!\n'
          f'Você \033[4mpassou{end}!')
else:
    print(f'Sua média foi {vermelho}{m}{end}!\n'
          f'Sendo \033[4minsuficiente{end}, você está {vermelho}REPROVADO{end}!')
