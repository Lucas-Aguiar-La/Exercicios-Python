# Dobro, Triplo e Raiz Quadrada:
verde = '\033[32m'
amarelo = '\033[33m'
end = '\033[m'
num = int(input('Digite um número: '))
print(f'O dobro de \033[4m{verde}{num}{end} é '
      f'{amarelo}{num * 2}{end}\n'
      f'O triplo {amarelo}{num * 3}{end}\n'
      f'E a raiz quadrada {amarelo}{num**(1/2):.2f}{end}')
