# Seno, Cosseno e Tangente:
import math
verde = '\033[32m'
amarelo = '\033[33m'
sub = '\033[4m'
end = '\033[m'
angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
print(f'O ângulo de {verde}{angulo}º{end} tem o {sub}SENO{end} de {amarelo}{seno:.2f}{end}')
cosseno = math.cos(math.radians(angulo))
print(f'O ângulo de {verde}{angulo}º{end} tem o {sub}COSSENO{end} de {amarelo}{cosseno:.2f}{end}')
tangente = math.tan(math.radians(angulo))
print(f'O ângulo de {verde}{angulo}º{end} tem a {sub}TANGENTE{end} de {amarelo}{tangente:.2f}{end}')
