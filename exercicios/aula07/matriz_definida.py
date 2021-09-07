'''
1) Escreva um programa que imprima na tela
    1,1 1,2 1,3 1,4 1,5 1,6
    2,1 2,2 2,3 2,4 2,5 2,6
    3,1 3,2 3,3 3,4 3,5 3,6
    4,1 4,2 4,3 4,4 4,5 4,6
    5,1 5,2 5,3 5,4 5,5 5,6.
'''

linhas = 1
colunas = 1

while linhas <= 5: # Do 1 até o 5

    linha = "" # String onde ficarão os valores de cada linha

    while colunas <= 6: # Do x,1 até o x,6
        linha += str(linhas) + "," + str(colunas) + " "
        colunas += 1

    print(linha)

    linhas += 1
    colunas = 1 # Reiniciar a contagem dos valores de cada linha
    del linha # Deleta-se a linha para reiniciar a escrita dos valores
