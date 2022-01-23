num_1 = input('Digite um Numero: ')
num_2 = input('Digite outro numero: ')

if num_1.isdigit() and num_2.isdigit():
    num_1 = int(num_1)
    num_2 = int(num_2)
    print(num_1+num_2)
else:
    print('Digite um numero VÁLIDO')
