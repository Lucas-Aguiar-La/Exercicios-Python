# Procurando uma String Dentro da Outra:
verde = '\033[32m'
sub = '\033[4m'
end = '\033[m'
nome = str(input(f'Qual é o seu {verde}{sub}nome '
                 f'completo{end}? ')).strip().upper()
silva = 'SILVA' in nome.split()
print(f'Seu nome tem {verde}{sub}Silva{end}? {silva}')
