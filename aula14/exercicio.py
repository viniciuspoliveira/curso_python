num_1 = input('Digite um numero inteiro: ')

if num_1.isdigit():
    num_1 = int(num_1)

    if num_1 % 2 == 0:
        print(f'{num_1} é par')
    else:
        print(f'{num_1} é impar')
else:
    print('Isso NÃO é um numero inteiro')