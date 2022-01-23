while True:
    cpf = input('Digite um CPF: ')
    novo_cpf = cpf [:-2]
    rev = 10
    total = 0
    for index in range(19):
        if index > 8:
            index -=9

        total += int(novo_cpf[index]) * rev

        rev -= 1
        if rev < 2:
           rev = 11
           dig = 11 - int(total % 11)

           if dig > 9:
               dig = 0
               total= 0
               novo_cpf += str(dig)

    if cpf == novo_cpf:
        print('CPF válido')
    else:
        print('CPF Inválido')