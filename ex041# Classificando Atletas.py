# Classificando Atletas:
from datetime import date
ano_atual = date.today().year
ano = int(input('Ano de nascimento: '))
idade = ano_atual - ano
print(f'O atleta tem {idade} anos.')
if -1 < idade < 10:
    print('Classificação: MIRIM')
elif 9 < idade < 15:
    print('Classificação: INFANTIL')
elif 14 < idade < 20:
    print('Classificação: JUNIOR')
elif idade == 20:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
