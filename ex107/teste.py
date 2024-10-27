from ex107 import moedas
from ex107.moedas import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moedas.moeda(p)} é {moedas.moeda(moedas.metade(p))}')
print(f'O dobro de {moedas.moeda(p)} é {moedas.moeda(moedas.dobro(p))}')
print(f'Aumentando 10%, temos R$ {moedas.moeda(moedas.aumentar(p, 10))}')
