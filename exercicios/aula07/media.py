'''
5.2) Escreva um programa que calcule a média
aritmética de um conjunto de números reais
fornecidos por um usuário. A entrada para quando
o usuário fornecer um valor negativo.
'''

cont = 0
acum = 0

while True:
    valor = (float(input("Insira um valor: ")))

    if valor < 0:
        break # O programa para ao receber um valor negativo

    cont += 1
    acum += valor

if cont == 0: # Se o programa parou antes de receber qualquer valor válido, cont é igual a 0
    print("Não foi inserido um valor positivo")
else:
    print("A média aritmética destes valores é: ", acum/cont)