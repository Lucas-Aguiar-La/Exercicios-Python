# Conversor de Medidas:
metro = int(input('Valor em metros: '))
cm = metro * 100
mm = cm * 10
amarelo = '\033[33m'
end = '\033[m'
print(f'Metros: {amarelo}{metro}{end}m\n'
      f'Centímetros: {amarelo}{cm}{end}cm\n'
      f'Milímetros: {amarelo}{mm}{end}mm')
