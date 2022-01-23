nome = 'Vinicius'
idade = 35
altura = 1.75
peso = 87
imc = peso/altura**2
import datetime
ano_atual = datetime.datetime.today().year

print(f'{nome} tem {idade}, {altura} de altura e pesa {peso}kg.')
print(f'O IMC de {nome} é {imc:.2f}.')
print(f'{nome} nasceu em {ano_atual-idade}.')