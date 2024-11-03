from itertools import count

num_maior = -999999
contador = 0

while True:
    numero = int(input('Digite um número ou -1 para parar: '))
    if numero == -1:
        break
    contador += 1
    if numero > num_maior:
        num_maior = numero

if contador != 0:
    print(f'O maior número é {num_maior}')
else:
    print('Você não inseriu nenhum número!')
