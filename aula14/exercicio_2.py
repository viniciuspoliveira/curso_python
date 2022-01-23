horario = input('Digite um numero entre 0 e 23: ')

if horario.isdigit():
    horario = int(horario)

    if horario < 0 or horario > 23:
        print('Digite um numero entre 0 e 23!')
    else:
        if horario <= 11:
            print('Bom dia!')
        elif horario <= 17:
            print('Boa tarde!')
        else:
            print('Boa noite!')
else:
    print('Erro, Digite um numero entre 0 e 23')