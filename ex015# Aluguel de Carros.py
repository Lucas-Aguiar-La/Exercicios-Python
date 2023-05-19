# Aluguel de Carros:
sub = '\033[4m'
amarelo = '\033[33m'
verde = '\033[32m'
end = '\033[m'
km = float(input(f'Quantos {sub}Km{end} foram percorridos? '))
dias = int(input(f'Durante quantos {sub}dias{end} o veículo foi alugado? '))
valor_a_pagar = dias * 60 + km * 0.15
print(f'O veículo rodou {sub}{km}Km{end} durante {sub}{dias} dias{end}...\n'
      f'O valor a ser pago é de {verde}R${valor_a_pagar:.2f}')
