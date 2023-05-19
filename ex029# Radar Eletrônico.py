# Radar Eletrônico:
red = '\033[31m'
yellow = '\033[33m'
sub = '\033[4m'
end = '\033[m'
velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print(f'{red}MULTADO! Você excedeu o limite permitido que é {sub}80Km/h{end}\n'
          f'{red}Você deve pagar uma multa de {sub}{yellow}R${(velocidade - 80) * 7:.2f}!{end}\n'
          f'{yellow}Tenha um bom dia e dirija com segurança!{end}')
else:
    print(f'{yellow}Tenha um bom dia e dirija com segurança!{end}')
