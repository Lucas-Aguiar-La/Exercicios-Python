# Verificando as Primeiras Letras de um Texto:
verde = '\033[32m'
sub = '\033[4m'
end = '\033[m'
cidade = str(input(f'Em que {verde}{sub}cidade{end}'
                   f' você nasceu? ')).strip().upper()
print(cidade[0:5] == 'SANTO')
