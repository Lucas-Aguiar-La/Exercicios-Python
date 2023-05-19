# Reajuste Salarial:
verde = '\033[32m'
s = '\033[4m'
end = '\033[m'
salario = float(input(f'Qual é o seu salário? {verde}R${end}'))
aumento = (salario * 15/100)
print(f'{verde}Parabéns{end}! Você recebeu um reajuste de {s}15%{end}!\n'
      f'Agora o seu salário é de {verde}R${salario + aumento:.2f}{end}')
