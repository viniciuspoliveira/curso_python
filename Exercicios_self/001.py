nome = input('Digite seu nome: ')
salario = float(input('Digite seu Salário: '))
imposto = 11
salario_liquido = salario - (salario * 11) /100

print(f'Seu salario liquido é de : R${salario_liquido}')