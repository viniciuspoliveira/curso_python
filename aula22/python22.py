var = ['luiz otavio', 'Joãozinho', 'maria' ]
comeca_com_j = False
for valor in var:
    if valor.lower().startswith('j'):
        break
else:
    print('Não existe uma palavra que começa com J')

