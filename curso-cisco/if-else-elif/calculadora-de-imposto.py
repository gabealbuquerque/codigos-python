# Calculadora de imposto
# Coletando a renda
renda = float(input('Digite a sua renda: '))

# Comparando a renda

if renda < 85528:
    taxa = renda * 0.18 - 556.02

taxa = round(taxa, 0)

print(f'A taxa é: {taxa} thalers.')
