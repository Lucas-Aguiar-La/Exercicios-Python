# Ímpar ou Par?
blue = '\033[34m'
end = '\033[m'
num = int(input('Me diga um número qualquer: '))
if num % 2 == 0:
    print(f'O número {num} é {blue}PAR{end}!')
else:
    print(f'O número {num} é {blue}ÍMPAR{end}!')
