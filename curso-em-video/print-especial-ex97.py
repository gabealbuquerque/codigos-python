def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)

 # Programa Principal
while True:
    msg = input('Digite uma mensagem: ')
    escreva(msg)
    opc = input('Quer continuar? [S/N] ').upper()
    if opc not in 'SN':
        print('ERRO! Digite apenas S ou N.')
    if opc == 'N':
        break
print('<< VOLTE SEMPRE! >>')
