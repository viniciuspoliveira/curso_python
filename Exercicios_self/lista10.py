sal_hora = float(input('Informe seu salário/hora: '))
trab_mes = float(input('Informe a quentidade de horas trabalhada: '))
sal_bruto = sal_hora * trab_mes
irpf = sal_bruto * 11 / 100
inss = sal_bruto * 8 / 100
sindicato = sal_bruto * 5 / 100
sal_liquido = sal_bruto - irpf - inss - sindicato

print(f'+ Salário Bruto: R$ {sal_bruto})
print(f'- IR (11%): R$ {irpf}')
print(f'- INSS (8%) : R$ {inss}')
print(f'- Sindicato (5%) : R$ {sindicato}')
print(f'= Salário Líquido : R$ {sal_liquido}')
