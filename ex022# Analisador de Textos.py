# Analisador de Textos:
from time import sleep
azul = '\033[34m'
verde = '\033[32m'
amarelo = '\033[33m'
sub = '\033[4m'
end = '\033[m'
nome = str(input('Digite seu nome completo: ')).strip()
print(f'{verde}Analisando...{end}')
mod = nome.split()
sleep(2)
print(f'Seu nome em maiúsculas: {azul}{sub}{nome.upper()}{end}\n'
      f'Seu nome em minúsculas: {azul}{sub}{nome.lower()}{end}\n'
      f'Ao todo, {sub}seu nome{end} possui {amarelo}{len(nome) - nome.count(" ")} letras{end};\n'
      f'E seu {sub}primeiro{end} nome tem {amarelo}{len (mod[0])} letras{end}!')
