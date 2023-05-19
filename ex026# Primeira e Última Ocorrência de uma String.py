# Primeira e Última Ocorrência de uma String:
verde = '\033[32m'
sub = '\033[4m'
end = '\033[m'
frase = str(input('Digite uma frase: ')).upper().strip()
print(f'A {verde}letra "A"{end} aparece {sub}{frase.count("A")}{end} vezes na frase.')
print(f'A {verde}primeira letra "A"{end} apareceu na posição'
      f' {sub}{frase.find("A") + 1}{end}...')
print(f'E a {verde}última letra "A"{end} na posição {sub}{frase.rfind("A") + 1}{end}!')
