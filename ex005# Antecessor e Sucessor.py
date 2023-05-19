# Antecessor e Sucessor:
verde = '\033[32m'
end = '\033[m'
num = int(input('Digite um número: '))
print(f'Com base no valor {verde}{num}{end}, seu antecessor é '
      f'{verde}{num - 1}{end}'
      f' e seu sucessor é {verde}{num + 1}{end}!')
