distancia_total = float(input('Digite a distância total (em km): '))
combustivel_gasto = float(input('Digite a quantidade de combustível gasto (em litros): '))
media = distancia_total / combustivel_gasto
print(f'O consumo médio ficou {media:.3f} km/l.')
