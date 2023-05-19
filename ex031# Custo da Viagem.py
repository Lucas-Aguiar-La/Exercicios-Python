# Custo da Viagem:
blue = '\033[34m'
green = '\033[32m'
end = '\033[m'
km = int(input('Qual a distância da sua viagem? '))
if km <= 200:
    print(f'Você fará uma viagem de {blue}{km:.1f}Km{end}.\n'
          f'E o preço da sua passagem será de {green}R${km * 0.50:.2f}{end}')
else:
    print(f'Você fará uma viagem de {blue}{km:.1f}Km{end}.\n'
          f'E o preço da sua passagem será de {green}R${km * 0.45:.2f}{end}')
