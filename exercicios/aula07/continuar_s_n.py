'''
5) Modifique o problema anterior para que, em
lugar do usuário informar quantos números irá
fornecer, o programa pergunte ao usuário se
deseja ou não fornecer mais um número inteiro.
Se a resposta for "s"(sim) o programa lê o
próximo número. Caso contrário (resposta "n"), o
programa termina.
'''

# Neste programa juntei as funções principais dos dois anteriores, dando o menor e maior valor numérico

valor_atual = (int(input("Insira um valor: ")))
max = valor_atual
min = valor_atual

continuar = input("Deseja inserir outro valor? (s/n) ")

while continuar == "s":
    valor_atual = (int(input("Insira outro valor: ")))

    if max < valor_atual: # Condição para pegar o maior valor
        max = valor_atual

    if min > valor_atual: # Condição para pegar o menor valor
        min = valor_atual

    continuar = input("Deseja inserir outro valor? (s/n) ")

print("O maior valor dentre os fornecidos é ", max, ", e o menor é ", min)