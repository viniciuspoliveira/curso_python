"""
Entrada de dados
"""

nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')
import datetime
ano_nascimento = datetime.datetime.today().year-int(idade)
print()
print(f'{nome} tem {idade} anos e nasceu no ano de {ano_nascimento}')