usuario = input('Digite o Usuario')
senha = input('Digite a Senha')

usuario_bd = 'vinicius'
senha_bd = '123456'

if usuario == usuario_bd and senha == senha_bd:
    print('Voce está logado')
else:
    print('senha ou usuario invalido')
