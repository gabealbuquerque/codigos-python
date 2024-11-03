# Programa que lê distância em metros e transforma em outras medidas
# Pedindo a distância em metros
distancia_m = float(input('Digite uma distância em metros: '))
# Convertendo em km
km = distancia_m / 1000
# Convertendo em Hm
hm = distancia_m / 100
# Convertendo em dam
dam = distancia_m / 10
# Convertendo em dm
dm = distancia_m * 10
# Convertendo em cm
cm = distancia_m * 100
# Convertendo em mm
mm = distancia_m * 1000
# Imprimindo resultado
print(f'A distância de {distancia_m}m corresponde a:\n{km}Km\n{hm}Hm\n{dam}Dam\n{dm}dm\n{cm}cm\n{mm}mm')
