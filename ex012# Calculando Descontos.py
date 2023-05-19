# Calculando Descontos:
verde = '\033[32m'
end = '\033[m'
s = '\033[4m'
produto = float(input('Qual é o preço do produto? R$'))
desc = (produto * 1.05) - produto
print(f'O produto custa R${produto:.2f}'
      f'\nHoje ele conta com uma promoção de {s}5%!{end}'
      f'\nFicando {verde}{s}R${produto - desc:.2f}{end}!')
