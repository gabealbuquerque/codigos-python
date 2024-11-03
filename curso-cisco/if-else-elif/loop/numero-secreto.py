secret_number = 777

print("""
+=============================+
| Bem vindo ao meu jogo!      |
| Insira um número inteiro    |
| e adivinhe o número secreto |
| Então, qual é o número?     |
+=============================+
""")

number = int(input('Digite o número secreto: '))

while number != secret_number:
    print('Ha ha! Você está preso no meu loop!')
    number = int(input('Digite o número secreto: '))

print('Muito bem! Você está livre agora!')
