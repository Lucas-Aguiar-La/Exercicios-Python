# Sorteando uma Ordem na Lista:
from random import shuffle
amarelo = '\033[33m'
sub = '\033[4m'
end = '\033[m'
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
lista = [a1, a2, a3, a4]
shuffle(lista)
print(f'A {sub}ordem{end} de apresentação será:\n'
      f'{amarelo}{lista}{end}!')
