# Maior e Menor Valor:
blue = '\033[34m'
end = '\033[m'
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O maior valor foi {blue}{maior}{end}\n'
      f'E o menor foi {blue}{menor}{end}')
