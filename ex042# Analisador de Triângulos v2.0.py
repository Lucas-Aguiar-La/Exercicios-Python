# Analisador de Triângulos v2.0:
blue = '\033[34m'
ciane = '\033[36m'
green = '\033[32m'
red = '\033[31m'
end = '\033[m'
print(f'{ciane}-=-{end}' * 11)
print(f'    {blue}ANALISADOR DE TRIÂNGULOS{end}')
print(f'{ciane}-=-{end}' * 11)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Tercerio segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'Os segmentos acima {green}PODEM FORMAR{end} um triângulo ', end='')
    if r1 == r2 == r3:
        print("EQUILÁTERO!")
    elif r1 != r2 != r3 != r1:
        print("ESCALENO!")
    else:
        print("ISÓSCELES!")
else:
    print(f'Os segmentos acima {red}NÃO PODEM{end} formar um triângulo!')
