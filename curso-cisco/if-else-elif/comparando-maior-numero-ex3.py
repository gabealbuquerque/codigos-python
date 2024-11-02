# Programa para comparar 5 numeros
# Lendo os números
number1 = int(input('Digite o 1º valor: '))
number2 = int(input('Digite o 2º valor: '))
number3 = int(input('Digite o 3º valor: '))
number4 = int(input('Digite o 4º valor: '))
number5 = int(input('Digite o 5º valor: '))

# Comparando os valores com a funcao max
largest_number = max(number1, number2, number3, number4, number5)

# Comparando os valores com a funcao min
smallest_number = min(number1, number2, number3, number4, number5)

# Imprimindo o resultado
print(f'O maior valor é {largest_number}')
print(f'O menor valor é {smallest_number}')
