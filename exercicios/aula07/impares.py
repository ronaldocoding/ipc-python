'''
1). Escreva um programa que imprima os número
ímpares de 1 até um valor informado por um
usuário.
'''

max = (int(input("Valor máximo: "))) # Busca por números ímpares até este número
i = 1 # Contador

while i <= max:
    if i % 2 == 1:
        print(i)
    i += 1