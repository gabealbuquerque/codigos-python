# Programa para ler sequencia de numeros
# e contar quantos são pares e impares
# termina quando o usuário digitar 0

# Contadores
impares = 0
pares = 0

# Lendo o primeiro numero
number = int(input('Digite um número ou digite 0 para parar: '))

# Se for diferente de zero, analise para ver se é par ou impar
while number != 0:
    # Verifique se é impar
    if number % 2 == 1:
        # Aumenta o contador do impar
        impares += 1
    else:
        # Aumenta o contador de par
        pares += 1
    # Leia o numero seguinte
    number = int(input('Digite um número ou digite 0 para parar: '))

# Imprimindo resultado
print(f'Números ímpares contam: {impares}')
print(f'Números pares contam: {pares}')
