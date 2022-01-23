idade = input('Digite sua idade: ')

if not idade.isnumeric():
    print('Digite a PORRA DO NUMERO CORRETO')
else:
    idade = int(idade)
    e_de_maior = idade >= 18
    msg = 'pode acessar' if e_de_maior else 'nao pode acessar'
    print(msg)
