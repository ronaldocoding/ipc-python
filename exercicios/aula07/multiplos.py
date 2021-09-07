'''
2) Escreva um programa para imprimir os
múltiplos de 3 de 0 até um valor informado por
um usuário.
'''

max = (int(input("Valor máximo: "))) # Busca por múltiplos de 3 até este número
i = 0 # Contador

while i < max:
    if i % 3 == 0: # Se i for divisível por 3, então também é múltiplo deste
        print(i)
    i += 1