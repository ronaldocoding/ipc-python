'''
1) Escreva um programa que peça dois números
inteiros e imprima a soma desses dois números na
tela.
'''

num1 = (int(input("Primeiro número: ")))
num2 = (int(input("Segundo número: ")))

# Uso de composição (%) para mostrar o resultado
print("%d + %d = %d" % (num1, num2, num1 + num2))