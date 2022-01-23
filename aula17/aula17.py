while False: #loop infinito
    nome = input('Qual o seu nome? ')
    print(f'Olá {nome}')

print('Essa parte não será executada')


x = 0
while x < 10:
    if x == 3:
        x = x + 1
        continue
    print(x)
    x = x + 1
print('Acabou')