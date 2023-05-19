# Conversor de Moeda:
verde = '\033[32m'
end = '\033[m'
real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 4.75
print(f'Valor em carteira: {verde}R${real:.2f}{end}'
      f'\nValor em dolar: {verde}US${dolar:.2f}{end}')
