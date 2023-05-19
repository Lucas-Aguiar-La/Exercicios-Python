# Sorteando um Item da Lista:
from random import choice
amarelo = '\033[33m'
sub = '\033[4m'
end = '\033[m'
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
lista = [a1, a2, a3, a4]
aluno = choice(lista)
print(f'O aluno {sub}SORTEADO{end} foi {sub}{amarelo}{aluno}{end}!')
