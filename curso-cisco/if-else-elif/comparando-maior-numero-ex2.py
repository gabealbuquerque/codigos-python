# Programa para comparar 3 números
# Lendo os números
number1 = int(input('Digite o primeiro número: '))
number2 = int(input('Digite o segundo número: '))
number3 = int(input('Digite o terceiro número: '))

# Comparando
if number1 > number2 and number3: largest_number = number1
if number2 > number1 and number3: largest_number = number2
if number3 > number1 and number2: largest_number = number3

# Imprimindo na tela
print(f'O maior valor é {largest_number}')
