usuario = input('Digite seu usario: ')
qtd_char = len(usuario)

if qtd_char < 6:
    print('Digite pelo menos seis caracteres')
else:
    print('Voce foi cadastrado no sistema')