# Índice de Massa Corporal:
peso = float(input("Informe o seu peso: "))
altura = float(input("Informe sua altura: "))
imc = peso / (altura ** 2)
if imc > 5:
    print(f"\nO seu IMC é de {imc:.1f}")
    if imc < 18.5:
        print("Você está ABAIXO do peso ideal.")
    elif 18.5 < imc < 25:
        print("Você está no peso IDEAL.")
    elif 25 < imc < 30:
        print("Você está em SOBREPESO.")
    elif 30 < imc < 40:
        print("Cuidado! Você está em OBESIDADE.")
    else:
        print("Obesidade MÓRBIDA!")
else:
    print("Algo deu errado! Tente novamente.")
