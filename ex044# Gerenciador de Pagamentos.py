# Gerenciador de Pagamentos:
rox = '\033[35m'
yell = '\033[33m'
end = '\033[m'
print(f'{rox}{"[LOJA DO FUSKITA]":=^40}{end}')
valor = float(input('Qual o valor das compras? R$'))
print('Formas de pagamento:\n'
      f'{yell}[ 1 ]{end} à vista no dinheiro ou pix\n'
      f'{yell}[ 2 ]{end} à vista no crédito\n'
      f'{yell}[ 3 ]{end} 2x no cartão\n'
      f'{yell}[ 4 ]{end} 3x ou mais no cartão\n')
escolha = int(input('Qual é a opção? '))
if escolha == 3:
    total = valor
    print(f'Você pagará 2 parcelas de R${valor / 2:.2f} cada.')
    print(f'Total: R${valor:.2f}')

elif escolha == 1:
    total = valor - (valor * 10 / 100)
    print(f'A sua compra de R${valor} será de R${total:.2f}')

elif escolha == 2:
    total = valor - (valor * 5 / 100)
    print(f'A sua compra de R${valor} será de R${total:.2f}')

elif escolha == 4:
    total = valor + (valor * 20 / 100)
    parcelas = int(input('Quantas parcelas? '))
    tot_parcelas = total / parcelas
    if parcelas >= 3:
        print(f'Você pagará {parcelas} parcelas de R${tot_parcelas:.2f}')
        print(f'Sua compra de R${valor:.2f} ficará R${total:.2f} no total.')
    else:
        print('Opção inválida, tente novamente...')

else:
    print('Algo deu errado, tente novamente...')


