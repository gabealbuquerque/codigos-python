# Programa que imprime uma mensagem
# Solicitando o nome da flor
name_of_flower = input('Digite o nome da flor: ')

# Comparando o valor
if name_of_flower == 'Spathiphyllum':
    print('Sim - Spathiphyllum é a melhor flor do mundo!')
elif name_of_flower == 'spathiphyllum':
    print('Não, eu quero um grande Spathiphyllum!')
else:
    print(f'Spathiphyllum! Não {name_of_flower}!')
