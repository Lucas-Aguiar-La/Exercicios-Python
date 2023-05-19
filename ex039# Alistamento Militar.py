# Alistamento Militar:
from datetime import date
ano_atual = date.today().year
ano_nasc = int(input('Ano de nascimento: '))
idade = ano_atual - ano_nasc
print(f'Quem nasceu em {ano_nasc} tem {idade} anos em {ano_atual}.')
if idade < 18:
    qto_falta = 18 - idade
    ano_alist = ano_atual + qto_falta
    print(f'Ainda falta(m) {qto_falta} ano(s) para se alistar.\n'
          f'Seu alistamento será em {ano_alist}.')
elif idade > 18:
    qto_passou = 18 - idade
    ano_alist = qto_passou + ano_atual
    print(f'Você já deveria ter se alistado em {ano_alist}.')
else:
    print(f'Você deve se alistar IMEDIATAMENTE!')
