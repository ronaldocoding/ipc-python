'''
4) Modifique o problema anterior para determinar
também o valor inteiro mínimo da sequência de
números fornecidos pelo usuário.
'''

entradas = (int(input("Total de entradas a serem fornecidas: "))) # Quantidade de números a serem lidos
i = 1

min = True
'''
Esta variável acima vai conter o valor menor. A princípio a iniciei como um boolean
pois não posso definir um valor númerico inicial, pois não se sabe quais valores serão
fornecidos pelo usuário.
'''

while i <= entradas:
    print(i, "º entrada:")
    valor_atual = (int(input()))

    if min is bool: # Se min for bool então ele ainda não possui nenhum falor numérico
        min = valor_atual
        i += 1
        continue # Este comando pula todos os comandos seguintes e volta para o começo da repetição

    # Se min já possui um valor numérico, não entrará na condição acima.

    if valor_atual < min:
        min = valor_atual

    i += 1

print("O menor valor dentre os fornecidos é ", min)