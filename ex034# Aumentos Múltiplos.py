# Aumentos Múltiplos:
yellow = '\033[33m'
green = '\033[32m'
end = '\033[m'
salario = float(input('Qual é o salário do funcionário? R$'))
if salario > 1250:
    aumento = salario + (salario * 10 / 100)
if salario <= 1250:
    aumento = salario + (salario* 15 / 100)
print(f'Quem ganhava {yellow}R${salario:.2f}{end} passa a ganhar {green}R${aumento:.2f}{end}')
