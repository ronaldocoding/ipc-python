'''
6) Modifique o programa anterior para calcular a
média ponderada dos valores e pesos fornecidos
por um usuário.
'''

cont = 0
acum = 0

while True:
    valor = (float(input("Insira um valor: ")))

    if valor < 0:
        break # O programa para ao receber um valor negativo

    peso = (int(input("Peso do valor anterior: ")))

    cont += peso
    acum += valor * peso # Cada valor é multiplicado pelo seu peso

if cont == 0: # Se o programa parou antes de receber qualquer valor válido, cont é igual a 0
    print("Não foi inserido um valor positivo")
else:
    print("A média aritmética destes valores é: ", acum/cont)