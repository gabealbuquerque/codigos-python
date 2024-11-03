# Programa que lê real e mostra quantos dólares pode comprar
# Pedindo valor em real
carteira = float(input('Quanto você tem na carteira? R$ '))
# Convertendo em dólar
dolar = carteira / 5.70
# Imprimindo resultado
print(f'R$ {carteira:.2f} = US$ {dolar:.2f}')
