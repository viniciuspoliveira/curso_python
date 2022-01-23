secreto = 'perfume'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Voce PERDEU!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print ('Ah isso nao vale. Digite apenas uma letra!')
        continue
    digitadas.append(letra)

    if letra in secreto:
        print(f'ACERTOU! A letra "{letra}" existe a letra na palavra secreta ')
    else:
        print(f'AFFFF. A letra "{letra}" Nao eiste na palavra secreta')
        digitadas.pop()



    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Que legal VOCE GANHOU!!!! A palavra era {secreto_temporario}')
        break
    else:
        print(f'A palvra secreta esta assim: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1
    print(f'Voce ainda tem {chances} chances')
    print()