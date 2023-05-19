# Primeiro e Último Nome de uma Pessoa:
nome_completo = str(input('Qual é o seu nome completo? ')).strip().capitalize()
nome_mod = nome_completo.split()
print(f'Prazer em te conhecer, {nome_mod[0]}!\n'
      f'Posso te chamar de '
      f'{nome_mod[len(nome_mod) - 1].capitalize()}, para facilitar?')
