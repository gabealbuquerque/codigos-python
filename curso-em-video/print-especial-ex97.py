def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)

 # Programa Principal
msg = input('Digite uma mensagem: ')
escreva(msg)
