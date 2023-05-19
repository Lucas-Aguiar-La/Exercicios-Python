# Conversor de Bases Numéricas:
und = '\033[4m'
end = '\033[m'
blue = '\033[34m'
red = '\033[31m'
num = int(input("Digite um número inteiro: "))
print(f'''Escolha uma das bases para conversão:
{blue}[ 1 ]{end} Converter para {und}BINÁRIO{end}
{blue}[ 2 ]{end} Converter para {und}OCTAL{end}
{blue}[ 3 ]{end} Converter para {und}HEXADECIMAL{end}''')
escolha = int(input('Sua opção: '))
if escolha == 1:
    print(f'\n{num} em BINÁRIO é {blue}{num:b}{end}')
elif escolha == 2:
    print(f'\n{num} em OCTAL é {blue}{num:o}{end}')
elif escolha == 3:
    print(f'{num} em HEXADECIMAL é {blue}{num:x}{end}')
else:
    print(f'{red}Opção inválida! Tente novamente.')
