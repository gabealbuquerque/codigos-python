# Calculadora para ano bissexto
# Coletando ano
ano = int(input('Digite o ano: '))

# Comparando ano

if ano < 1582:
    print('Não dentro do período calendário gregoriano.')
else:
    if ano % 4 != 0:
        print('Ano comum!')
    elif ano % 100 != 0:
        print('Ano bissexto!')
    elif ano % 400 != 0:
        print('Ano comum!')
    else:
        print('Ano bissexto!')
