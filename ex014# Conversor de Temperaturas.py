# Conversor de Temperaturas:
azul = '\033[34m'
sub = '\033[4m'
end = '\033[m'
c = float(input('Informe a temperatura em ºC: '))
f = c * 1.8 + 32
print (f'A temperatura de {azul}{sub}{c}ºC{end} '
       f'corresponde a {azul}{sub}{f}ºF{end}!')
