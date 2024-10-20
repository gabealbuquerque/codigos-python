def linha(l):
    print('-' * 30)
    print(l)
    print('-' * 30)
def area(larg, comp):
    area = larg * comp
    print(f'A área de um terreno {larg:.1f}x{comp:.1f} é de {area}m².')
    
# Programa principal
linha('     Controle de Terrenos')
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
