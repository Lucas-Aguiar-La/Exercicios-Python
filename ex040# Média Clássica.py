# Média Clássica:
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print(f'A média foi de {media:.1f}')
if 7 < media < 10:
    print('Você está APROVADO!')
elif 5 < media < 7:
    print('Você está de RECUPERAÇÃO!')
elif -1 < media < 5:
    print('Você está REPROVADO!')
else:
    print('Algo deu errado... Tente novamente.')
