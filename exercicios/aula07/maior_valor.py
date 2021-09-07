'''
3) Escreva um programa que determine qual o
valor inteiro máximo de uma sequência de
números fornecidos por um usuário. O usuário
deve informar quantos números irá fornecer.
'''

entradas = (int(input("Total de entradas a serem fornecidas: "))) # Quantidade de números a serem lidos
i = 1

max = True
'''
Esta variável acima vai conter o valor máximo. A princípio a iniciei como um boolean
pois não posso definir um valor númerico inicial, pois não se sabe quais valores serão
fornecidos pelo usuário.
'''

while i <= entradas:
    print(i, "º entrada:")
    valor_atual = (int(input()))

    if max is bool: # Se max for bool então ele ainda não possui nenhum falor numérico
        max = valor_atual
        i += 1
        continue # Este comando pula todos os comandos seguintes e volta para o começo da repetição

    # Se max já possui um valor numérico, não entrará na condição acima.

    if valor_atual > max:
        max = valor_atual

    i += 1

print("O maior valor dentre os fornecidos é ", max)