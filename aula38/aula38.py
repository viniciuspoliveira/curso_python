print()
print('Texto explicativo')

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2?',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '5',
            'd': '6',
        },
        'resposta_certa': 'b'
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3*2?',
        'respostas': {
            'a': '4',
            'b': '10',
            'c': '6',
            'd': '8',
        },
        'resposta_certa': 'c'
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 1+2?',
        'respostas': {
            'a': '4',
            'b': '3',
            'c': '6',
            'd': '8',
        },
        'resposta_certa': 'b'
    },
    'Pergunta 4': {
        'pergunta': 'Quanto é 1-1?',
        'respostas': {
            'a': '0',
            'b': '10',
            'c': '6',
            'd': '100',
        },
        'resposta_certa': 'a'
    },
    'Pergunta 5': {
        'pergunta': 'Quanto é 8/4?',
        'respostas': {
            'a': '4',
            'b': '9',
            'c': '6',
            'd': '2',
        },
        'resposta_certa': 'd'
    },
}
respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Respostas: ')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Sua resposta: ')
    if resposta_usuario == pv['resposta_certa']:
        print('EHHHHH! Voce acertou')
        respostas_certas +=1
    else:
        print('Imbecil, voce errou')
    print()
qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

print(f'Voce acertou {respostas_certas} resposta(s).')
print(f'Sua porcentagem de acerto foi de {porcentagem_acerto}%.')