# Programa para rodar diversas vezes
# Atribuindo um valor
largest_number = -9999999

# Insira o primeiro valor
number = int(input('Digite um número ou digite -1 para parar: '))

# Se o número for diferente de -1, execute:
while number != -1:
    # O número é maior que o maior_numero?
    if number > largest_number:
        # Se sim, atualize o valor do maior_numero
        largest_number = number
    # Insira o proximo numero
    number = int(input('Digite um número ou digite -1 para parar: '))

# Imprima o maior número
print(f'O maior número é: {largest_number}')
print('<< VOLTE SEMPRE >>')
4