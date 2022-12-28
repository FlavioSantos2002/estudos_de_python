#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês,
# sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato,
# faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
a = float(input('salário por hora: '))
b = float(input('horas trabalhadas no mês no formato (horas.minutos: '))
snm = a*b
sl = snm - snm*0.11 - 0.08*snm - 0.05*snm
print('salario bruto:R$: {}\nIR: R${:17}\nINSS: R${:15}\nSindicato: R${:10}\nSalario liquido: R${:4}'.format(snm, snm*0.11, 0.08*snm, 0.05*snm, (snm - snm*0.11 - 0.08*snm- 0.05*snm) ))




