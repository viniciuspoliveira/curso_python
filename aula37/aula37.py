# d1 = {
#     'chave1' : 'valor',
#     'chave2': 'outro valor',
#     'chave3': 'Tupla',
# }
#
# for k,v in d1.items():
#     print(k,v)

# clientes = {
#     'cliente1': {
#         'nome': 'Vinicius',
#         'sobrenome': 'Pinheiro',
#     },
#     'cliente2': {
#         'nome': 'Joao',
#         'sobrenome': 'Moreira',
#     },
#     'cliente3': {
#         'nome': 'Fernando',
#         'sobrenome': 'Penha',
#     },
#     'cliente4': {
#         'nome': 'Adriana',
#         'sobrenome': 'Penha',
#     },
#
# }
#
# for clintes_k, clientes_v in clientes.items():
#     print(f'Exibindo {clintes_k}')
#     for dados_k, dados_v in clientes_v.items():
#         print(f'\t{dados_k} = {dados_v}')


# d1 = {1: 'a', 2: 'b', 3: 'c', 'd': ['Luiz', 'otavio']}
# v =d1.copy()
#
# v[1] = 'Luiz'
# v['d'] = ('otavio', 'luiz')
# print(d1)
# print(v)

lista = [
    ['c1', 1],
    ['c2', 2],
    ['c3', 3],
]

d1 = dict(lista)
print(d1)