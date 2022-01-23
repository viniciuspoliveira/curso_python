

nome = 'Vinicius Pinheiro'
idade = 35
altura = 1.75
peso = 85
imc = peso/(altura*altura)

print(nome, 'tem', idade, 'de idade e seu IMC é de ',imc)
print(f'{nome} tem {idade}, de idade e seu IMC é {imc:.2f}')
print('{} tem {} anos e seus imc é {:.2f}'.format(nome,idade,imc))