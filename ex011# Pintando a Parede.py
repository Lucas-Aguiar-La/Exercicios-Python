# Pintando a Parede:
amarelo = '\033[33m'
azul = '\033[34m'
end = '\033[m'
altura = float(input('Qual é a altura da parede? '))
largura = float(input('Qual é a largura da parede? '))
area = altura * largura
tinta = area / 2
print(f'Sua parede tem {amarelo}{altura}{end} de altura '
      f'e {amarelo}{largura}{end} de largura.'
      f'\nSendo assim, sua área é de {amarelo}{area:.3}m²{end}'
      f'\n\033[4m{tinta}l{end} de tinta são necessários '
      f'para pintar {amarelo}{area:.3}m²{end}')
