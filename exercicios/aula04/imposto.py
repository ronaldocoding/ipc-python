"""
1) Escreva uma expressão para determinar se uma pessoa deve ou não pagar impostos. Considere que pagam imposto pessoas
cujo salário é maior que R$ 1200, 00.
"""

salario = int(input('Salário: ')) #Recebe o valor inteiro do usuário
pagaImposto = salario > 1200 #Verifica se é maior que R$ 1200, 00

print('A pessoa paga imposto? ' + str(pagaImposto)) #Função str() converte o valor para uma string
