string = 'O brasil é o oooo país do futebol, o Brasil é penta.'
lista_1 = string.split(' ')
lista_2 = string.split(',')

palavra = ''
contagem = 0
for valor in lista_1:
    qtd_vezes = lista_1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'a palavra que apareceu mais vezes é {palavra} ({contagem}x)')