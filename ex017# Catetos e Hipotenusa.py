# Catetos e Hipotenusa:
sub = '\033[4m'
verde = '\033[32m'
amarelo = '\033[33m'
end = '\033[m'
c_oposto = float(input(f'Comprimento do {sub}cateto oposto{end}: '))
c_adjacente = float(input(f'Comprimento do {sub}cateto adjacente{end}: '))
hip = (c_oposto ** 2 + c_adjacente ** 2) ** (1/2)
print(f'O valor da {amarelo}{sub}hipotenusa{end} será {verde}{hip:.2f}{end}')
