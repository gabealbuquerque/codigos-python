# Programa para comparar dois números.
# Ler dois números
number1 = int(input('Digite o primeiro número: '))
number2 = int(input('Digite o segundo número: '))

# Comparando o valor maior
if number1 > number2: larger_number = number1
else: larger_number = number2

# Imprimindo o resultado
print(f'O maior número é: {larger_number}.')
5