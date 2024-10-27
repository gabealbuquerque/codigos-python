from ex107 import moedas

p = float(input('Digite o preço: R$ '))
print(f'A metade de R$ {p:.2f} é R$ {moedas.metade(p):.2f}')
print(f'O dobro de R$ {p:.2f} é R$ {moedas.dobro(p):.2f}')
print(f'Aumentando 10%, temos R$ {moedas.aumentar(p, 10):.2f}')
