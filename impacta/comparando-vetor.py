menor = 0
num = int(input('Digite um número: '))
lista = 10 * [0]
i = 0
while i <= 10:
    lista[i] = num
    i += 1
    if num < menor:
        menor = num
print(f'O menor valor é {menor}')
