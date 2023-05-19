# Aprovando Empréstimo:
green = '\033[32m'
red = '\033[31m'
und = '\033[4m'
end = '\033[m'
casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o salário do comprador? R$'))
anos = int(input('Quanto anos de financiamento? '))
prestacao = casa / (anos * 12)
minimo = salario * 30/100 # O mínimo é 30% do salário.
print(f'Uma casa no valor de {green}R${casa:.2f}{end} em {anos} anos\n'
      f'tem uma prestação de {green}R${prestacao:.2f}{end}')
if prestacao >= minimo:
    print(f'O empréstimo foi {red}{und}NEGADO{end}!')
else:
    print(f'O empréstimo foi {green}{und}APROVADO{end}!')
